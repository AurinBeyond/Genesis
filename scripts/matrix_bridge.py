"""
Matrix Aurin Bridge

Public API:
    create_payment_link(product_name, price_eur) -> str
        Idempotent: reuses an existing product, price, and payment link when
        one already exists in Stripe, creating only what is missing.
        Returns the shareable payment-link URL.

    create_autonomous_product(name, price_eur, file_id, success_url) -> str | None
        Builds on create_payment_link. Adds an after_completion redirect on the
        Stripe payment link and optionally verifies a SendOwl product for digital
        delivery. Returns the payment-link URL or None on error.

Required environment variables:
    STRIPE_SECRET_KEY     — set as a GitHub Secret, never hardcoded.
    SENDOWL_API_KEY       — optional; needed only for SendOwl delivery check.
    SENDOWL_API_SECRET    — optional; needed only for SendOwl delivery check.
"""
import os
import stripe
import requests
from requests.auth import HTTPBasicAuth

# Defaults used by the Bridge Autopilot workflow
_DEFAULT_PRODUCT_NAME = "Matrix Aurin: Genesis Alpha Access"
_DEFAULT_PRICE_EUR = 22.0
_CURRENCY = "eur"
_DEFAULT_SUCCESS_URL = "https://aurinbeyond.com/success"
_SENDOWL_PRODUCTS_URL = "https://www.sendowl.com/api/v1/products"


def _resolve_api_key() -> str:
    key = os.getenv("STRIPE_SECRET_KEY", "").strip()
    if not key:
        raise EnvironmentError(
            "STRIPE_SECRET_KEY is not set. "
            "Add it as a GitHub Secret or export it locally."
        )
    return key


def _find_existing_product(name: str) -> "stripe.Product | None":
    """Return the first active product with the given name, or None."""
    for product in stripe.Product.list(active=True, limit=100).auto_paging_iter():
        if product.name == name:
            return product
    return None


def _find_existing_price(product_id: str, unit_amount: int) -> "stripe.Price | None":
    """Return the first active EUR price matching unit_amount for the product, or None."""
    for price in stripe.Price.list(product=product_id, active=True, limit=100).auto_paging_iter():
        if price.unit_amount == unit_amount and price.currency == _CURRENCY:
            return price
    return None


def _find_existing_payment_link(price_id: str) -> "stripe.PaymentLink | None":
    """Return the first active payment link that contains the given price, or None."""
    for link in stripe.PaymentLink.list(active=True, limit=100).auto_paging_iter():
        expanded = stripe.PaymentLink.retrieve(link.id, expand=["line_items"])
        items = getattr(expanded, "line_items", None)
        if items:
            for item in items.data:
                if getattr(item, "price", None) and item.price.id == price_id:
                    return link
    return None


def create_payment_link(
    product_name: str,
    price_eur: float,
    success_url: str | None = None,
) -> str:
    """
    Idempotently create (or reuse) a Stripe product, price, and payment link.

    Args:
        product_name: Display name for the Stripe product.
        price_eur:    Price in euros (e.g. 22 for 22.00 EUR).
        success_url:  Optional URL to redirect to after a successful payment.
                      When provided the payment link is created with
                      after_completion.type=redirect. Ignored for existing links.

    Returns:
        The shareable payment-link URL.

    Raises:
        EnvironmentError: STRIPE_SECRET_KEY is not set.
        SystemExit:       A Stripe API error occurred.
    """
    stripe.api_key = _resolve_api_key()
    unit_amount = int(price_eur * 100)

    try:
        # --- Product ---
        product = _find_existing_product(product_name)
        if product:
            print(f"product_id: {product.id} (existing)")
        else:
            product = stripe.Product.create(
                name=product_name,
                description="Matrix Aurin Genesis System - Autonomous Delivery",
            )
            print(f"product_id: {product.id} (created)")

        # --- Price ---
        price = _find_existing_price(product.id, unit_amount)
        if price:
            print(f"price_id: {price.id} (existing)")
        else:
            price = stripe.Price.create(
                product=product.id,
                unit_amount=unit_amount,
                currency=_CURRENCY,
            )
            print(f"price_id: {price.id} (created)")

        # --- Payment link ---
        payment_link = _find_existing_payment_link(price.id)
        if payment_link:
            print(f"payment_link: {payment_link.url} (existing)")
        else:
            create_kwargs: dict = {
                "line_items": [{"price": price.id, "quantity": 1}],
            }
            if success_url:
                create_kwargs["after_completion"] = {
                    "type": "redirect",
                    "redirect": {"url": success_url},
                }
            payment_link = stripe.PaymentLink.create(**create_kwargs)
            print(f"payment_link: {payment_link.url} (created)")

        return payment_link.url

    except stripe.error.AuthenticationError:
        raise SystemExit(
            "Authentication error: STRIPE_SECRET_KEY is invalid or revoked. "
            "Verify you are using the correct key (sk_live_... or sk_test_...)."
        )
    except stripe.error.StripeError as exc:
        raise SystemExit(f"Stripe error: {exc}")


def create_autonomous_product(
    name: str,
    price_eur: float,
    file_id: str | None = None,
    success_url: str = _DEFAULT_SUCCESS_URL,
) -> str | None:
    """
    Create a Stripe product with an after_completion redirect and optionally
    verify a SendOwl product for digital delivery.

    Args:
        name:        Display name for the product.
        price_eur:   Price in euros.
        file_id:     SendOwl product/file ID to verify delivery readiness.
                     Pass None to skip the SendOwl check.
        success_url: URL to redirect customers after a successful payment.

    Returns:
        The shareable payment-link URL, or None on error.
    """
    try:
        print(f"Starting agent: creating product '{name}'...")

        url = create_payment_link(name, price_eur, success_url=success_url)

        # --- SendOwl delivery check (optional) ---
        sendowl_key = os.getenv("SENDOWL_API_KEY", "").strip()
        sendowl_secret = os.getenv("SENDOWL_API_SECRET", "").strip()

        if sendowl_key and sendowl_secret:
            if file_id:
                resp = requests.get(
                    f"{_SENDOWL_PRODUCTS_URL}/{file_id}",
                    auth=HTTPBasicAuth(sendowl_key, sendowl_secret),
                    timeout=10,
                )
                if resp.ok:
                    print(f"SendOwl: product {file_id} verified for delivery")
                else:
                    print(
                        f"SendOwl: product {file_id} check returned {resp.status_code} — "
                        f"{resp.text[:200]}"
                    )
            else:
                print("SendOwl: credentials present; no file_id supplied, skipping check")

        print(f"name: {name}")
        print(f"price: {price_eur} EUR")
        print(f"payment_link: {url}")

        return url

    except (EnvironmentError, SystemExit) as exc:
        print(f"Agent error: {exc}")
        return None


def run_bridge():
    """Entry point for the Bridge Autopilot workflow."""
    url = create_autonomous_product(_DEFAULT_PRODUCT_NAME, _DEFAULT_PRICE_EUR)
    if url:
        print(f"url: {url}")


if __name__ == "__main__":
    run_bridge()
