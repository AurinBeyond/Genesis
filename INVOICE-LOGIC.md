# INVOICE LOGIC v1.0

**Brand:** Pure Soul Life
**Task ID:** FIN-001
**Layer:** Payment / Trust / Legal
**Status:** Active

---

## PURPOSE

This document defines how invoices are structured for Pure Soul Life transactions.

An invoice is issued on request or when required by the client for accounting or legal purposes.

---

## WHEN AN INVOICE IS ISSUED

- Upon client request after a confirmed purchase
- When required for business or tax documentation purposes
- Not issued automatically — the standard receipt (sent by Gumroad) serves as default purchase confirmation

To request an invoice, the client contacts: `contact.puresoul@proton.me` with their order ID.

---

## BASE STRUCTURE

Every invoice must contain the following fields:

---

### 1. SELLER INFORMATION

| Field | Value |
|-------|-------|
| Seller name | Pure Soul Life |
| Operating brand | Pure Soul Life / AurinBeyond |
| Contact | contact.puresoul@proton.me |

---

### 2. CLIENT INFORMATION

| Field | Value |
|-------|-------|
| Client name | As provided by the client |
| Client email | Email used at checkout |
| Client address | If provided by client |

If the client has not provided billing details, the invoice is issued to the email address on the order.

---

### 3. SERVICE DESCRIPTION

| Field | Value |
|-------|-------|
| Product / Service | As named in the Gumroad listing at time of purchase |
| Description | Digital content or personal development service |
| Delivery format | Digital — immediate access upon payment |

---

### 4. PRICING

| Field | Value |
|-------|-------|
| Unit price | In NOK |
| Quantity | 1 |
| Total | In NOK |
| Currency | NOK (Norwegian Kroner) |

All amounts are stated in NOK. This is the billing currency.

If a display conversion was shown at the time of purchase, it is not reproduced on the invoice. The invoice shows NOK only.

---

### 5. TAX AND VAT

Pure Soul Life is a digital content business operating on Gumroad.

VAT handling:

- Gumroad collects and remits VAT where applicable under its Merchant of Record model
- Pure Soul Life does not separately charge or administer VAT
- If the client requires VAT documentation, they contact Gumroad directly using the transaction ID

**Invoice statement (required):**

> VAT, if applicable, is collected and remitted by Gumroad as Merchant of Record.
> Pure Soul Life does not issue separate VAT invoices.
> For VAT-specific documentation, contact Gumroad support with your transaction ID.

---

### 6. PAYMENT STATUS

Every invoice must carry one of three statuses:

| Status | Meaning |
|--------|---------|
| PAID | Payment confirmed. Access granted. |
| PENDING | Payment not yet confirmed. Access withheld. |
| FAILED | Payment declined. No order created. |

Standard invoices issued post-purchase carry status: **PAID**.

---

### 7. INVOICE REFERENCE

| Field | Value |
|-------|-------|
| Invoice number | Order ID from Gumroad |
| Invoice date | Date of purchase |
| Payment date | Same as invoice date (immediate processing) |

---

### 8. LEGAL NOTE

The following statement must appear on every invoice:

> Pure Soul Life provides informational and personal development services.
> No specific outcomes or results are guaranteed.
> This invoice is subject to the Terms of Service and Client Agreement available at the point of purchase.
> The maximum liability is limited to the amount stated on this invoice.

---

## CURRENCY RULE

NOK is the official billing currency.

If a client's bank converted the payment to another currency, that conversion is not reflected on the invoice.

The invoice states only:
- the NOK amount
- the confirmation that Gumroad processed the transaction

---

## INVOICE FORMAT

- Issued as a PDF or structured plain text document
- Must be legible on mobile and desktop
- No images required for the invoice to be valid
- All amounts formatted as: `[number] NOK` (e.g., `497 NOK`)

---

## CONNECTED DOCUMENTS

- `RECEIPT-STANDARD.md` — automated post-purchase receipt
- `laws/PRICING-CURRENCY-POLICY.md` — currency and conversion rules
- `laws/CLIENT-AGREEMENT.md` — referenced in legal note
- `CLIENT-COMMUNICATION.md` — how invoice requests are handled
- `USER-FLOW.md` → Step 5 (PAYMENT) — the transaction this invoice documents

---

STATUS: Active // Pure Soul Life // GENESIS Payment Layer
