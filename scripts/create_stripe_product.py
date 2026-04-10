import os
import stripe

# API key must be set via the STRIPE_SECRET_KEY environment variable.
# For local use: export STRIPE_SECRET_KEY=sk_test_...
# For CI/GitHub Actions: add STRIPE_SECRET_KEY as a GitHub Secret.
# Never hardcode the key in source code.
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

if not stripe.api_key:
    raise EnvironmentError(
        "STRIPE_SECRET_KEY environment variable is not set. "
        "Export it before running this script."
    )


def create_matrix_product():
    try:
        product = stripe.Product.create(
            name="Matrix Aurin: Genesis Alpha Access",
            description="Esimene samm autonoomse süsteemi suunas. Ligipääs Genesis koodile.",
        )

        price = stripe.Price.create(
            product=product.id,
            unit_amount=2200,  # 2200 senti = 22 EUR
            currency="eur",
        )

        payment_link = stripe.PaymentLink.create(
            line_items=[{"price": price.id, "quantity": 1}],
        )

        print(f"product_id: {product.id}")
        print(f"price_id: {price.id}")
        print(f"payment_link: {payment_link.url}")

    except stripe.error.AuthenticationError:
        raise SystemExit(
            "Autentimise viga: STRIPE_SECRET_KEY on vigane või kehtetu. "
            "Kontrolli, et kasutad õiget võtit (sk_live_... või sk_test_...)."
        )
    except stripe.error.StripeError as e:
        raise SystemExit(f"Stripe viga: {e}")


if __name__ == "__main__":
    create_matrix_product()
