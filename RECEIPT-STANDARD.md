# RECEIPT STANDARD v1.0

**Brand:** Pure Soul Life
**Task ID:** FIN-001
**Layer:** Payment / Trust / Legal
**Status:** Active

---

## PURPOSE

This document defines what every client receives immediately after a successful payment.

The receipt must allow the client to confirm:
- what they paid
- the exact amount
- what happens next

without needing to contact support.

---

## DELIVERY

**Sent by:** Gumroad (automated)
**Trigger:** Successful payment confirmation
**Channel:** Email to the address entered at checkout
**Timing:** Immediate — within minutes of payment

---

## RECEIPT FIELDS (REQUIRED)

Every receipt must contain all of the following:

---

### 1. TRANSACTION DETAILS

| Field | Value |
|-------|-------|
| Product / Service name | As listed on Gumroad at time of purchase |
| Date and time | UTC timestamp of transaction |
| Transaction ID | Unique order ID issued by Gumroad |
| Seller | Pure Soul Life |

---

### 2. PAYMENT DETAILS

| Field | Value |
|-------|-------|
| Amount charged | In NOK (Norwegian Kroner) |
| Display currency | If shown, clearly marked as estimate only |
| Payment method | Card or other method used at checkout |
| Processor | Gumroad |

---

### 3. CURRENCY CLARITY STATEMENT

The following statement must be present on every receipt, verbatim or equivalent:

> **Base currency: NOK (Norwegian Kroner)**
> The amount charged was processed in NOK.
> If your bank account is in a different currency, your bank applied a conversion rate.
> Pure Soul Life does not control bank conversion rates or any additional fees charged by your provider.

---

### 4. CLIENT MESSAGE

The receipt must include a short, direct confirmation of what happens next:

> Your purchase is confirmed.
> You will receive access to [Product Name] at this email address.
> If you do not receive the access link within 15 minutes, check your spam folder.
> For support: contact.puresoul@proton.me — include your order ID.

---

### 5. SUPPORT CONTACT

| Field | Value |
|-------|-------|
| Support email | contact.puresoul@proton.me |
| Response time | Within 24 hours |

---

## FORMAT REQUIREMENTS

- Plain text or minimal HTML — readable on all devices including mobile
- No images required for the receipt to be understood
- No ambiguous abbreviations
- All amounts written as: `[number] NOK` (e.g., `497 NOK`)
- Converted amounts written as: `~[number] [CURRENCY] (estimate)` (e.g., `~44 EUR (estimate)`)

---

## WHAT THE RECEIPT DOES NOT INCLUDE

- Guarantees of results
- Price negotiations or adjustments
- Unsolicited product offers

---

## CONNECTED DOCUMENTS

- `laws/PRICING-CURRENCY-POLICY.md` — currency and conversion rules
- `DELIVERY-SYSTEM.md` — what happens after the receipt is sent
- `CLIENT-COMMUNICATION.md` — how support responds to receipt-related queries
- `INVOICE-LOGIC.md` — invoice structure for clients who request one

---

STATUS: Active // Pure Soul Life // GENESIS Payment Layer
