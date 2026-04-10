"""
Matrix Aurin Bridge

Public API:
    create_payment_link(product_name, price_eur) -> str
        Idempotent: reuses an existing product, price, and payment link when
        one already exists in Stripe, creating only what is missing.
        Returns the shareable payment-link URL.

Required environment variable:
    STRIPE_SECRET_KEY  — set as a GitHub Secret, never hardcoded.
"""
import os
import stripe

# Defaults used by the Bridge Autopilot workflow
_DEFAULT_PRODUCT_NAME = "Matrix Aurin: Genesis Alpha Access"
_DEFAULT_PRICE_EUR = 22.0
_CURRENCY = "eur"


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


def create_payment_link(product_name: str, price_eur: float) -> str:
    """
    Idempotently create (or reuse) a Stripe product, price, and payment link.

    Args:
        product_name: Display name for the Stripe product.
        price_eur:    Price in euros (e.g. 22 for 22.00 EUR).

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
            product = stripe.Product.create(name=product_name)
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
            payment_link = stripe.PaymentLink.create(
                line_items=[{"price": price.id, "quantity": 1}],
            )
            print(f"payment_link: {payment_link.url} (created)")

        return payment_link.url

    except stripe.error.AuthenticationError:
        raise SystemExit(
            "Authentication error: STRIPE_SECRET_KEY is invalid or revoked. "
            "Verify you are using the correct key (sk_live_... or sk_test_...)."
        )
    except stripe.error.StripeError as exc:
        raise SystemExit(f"Stripe error: {exc}")


def run_bridge():
    """Entry point for the Bridge Autopilot workflow."""
    url = create_payment_link(_DEFAULT_PRODUCT_NAME, _DEFAULT_PRICE_EUR)
    print(f"url: {url}")


if __name__ == "__main__":
    run_bridge()
