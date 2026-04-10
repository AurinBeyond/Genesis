"""
Matrix Aurin Bridge

Idempotent: looks up an existing active product and price before creating new ones.
Run on every push to main via the Matrix Aurin Bridge Autopilot workflow.

Required environment variable:
    STRIPE_SECRET_KEY  — set as a GitHub Secret, never hardcoded.
"""
import os
import stripe

PRODUCT_NAME = "Matrix Aurin: Genesis Alpha Access"
PRICE_AMOUNT = 2200  # cents (22 EUR)
PRICE_CURRENCY = "eur"


def _resolve_api_key() -> str:
    key = os.environ.get("STRIPE_SECRET_KEY", "").strip()
    if not key:
        raise EnvironmentError(
            "STRIPE_SECRET_KEY is not set. "
            "Add it as a GitHub Secret or export it locally."
        )
    return key


def _find_existing_product() -> "stripe.Product | None":
    """Return the first active product matching PRODUCT_NAME, or None."""
    for product in stripe.Product.list(active=True, limit=100).auto_paging_iter():
        if product.name == PRODUCT_NAME:
            return product
    return None


def _find_existing_price(product_id: str) -> "stripe.Price | None":
    """Return the first active recurring-or-one-time price for the product, or None."""
    for price in stripe.Price.list(product=product_id, active=True, limit=100).auto_paging_iter():
        if price.unit_amount == PRICE_AMOUNT and price.currency == PRICE_CURRENCY:
            return price
    return None


def _find_existing_payment_link(price_id: str) -> "stripe.PaymentLink | None":
    """Return the first active payment link containing the given price, or None."""
    for link in stripe.PaymentLink.list(active=True, limit=100).auto_paging_iter():
        expanded = stripe.PaymentLink.retrieve(link.id, expand=["line_items"])
        items = getattr(expanded, "line_items", None)
        if items:
            for item in items.data:
                if getattr(item, "price", None) and item.price.id == price_id:
                    return link
    return None


def run_bridge():
    stripe.api_key = _resolve_api_key()

    try:
        # --- Product ---
        product = _find_existing_product()
        if product:
            print(f"product_id: {product.id} (existing)")
        else:
            product = stripe.Product.create(
                name=PRODUCT_NAME,
                description="Esimene samm autonoomse süsteemi suunas. Ligipääs Genesis koodile.",
            )
            print(f"product_id: {product.id} (created)")

        # --- Price ---
        price = _find_existing_price(product.id)
        if price:
            print(f"price_id: {price.id} (existing)")
        else:
            price = stripe.Price.create(
                product=product.id,
                unit_amount=PRICE_AMOUNT,
                currency=PRICE_CURRENCY,
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

    except stripe.error.AuthenticationError:
        raise SystemExit(
            "Authentication error: STRIPE_SECRET_KEY is invalid or revoked. "
            "Verify you are using the correct key (sk_live_... or sk_test_...)."
        )
    except stripe.error.StripeError as exc:
        raise SystemExit(f"Stripe error: {exc}")


if __name__ == "__main__":
    run_bridge()
