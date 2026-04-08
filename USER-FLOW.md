# USER FLOW v1.0

**Brand:** Pure Soul Life
**Task ID:** FLOW-001
**Layer:** Business Logic
**Status:** Active

---

## SINGLE PATH

```
ENTRY → PAGE → DECISION → ACTION → PAYMENT → CONFIRMATION → DELIVERY → FOLLOW-UP → NEXT STEP
```

---

## STEP 1 — ENTRY

**Source:** The user arrives via one of the following:

- Social media post or story (Instagram, TikTok, or similar)
- Direct link shared in message or email
- Search result or referral

**Landing destination:** `index.html`

---

## STEP 2 — PAGE

**Page sequence the user moves through:**

1. `index.html` — Brand introduction. User reads the core message and identity of Pure Soul Life.
2. `vsl.html` — Video or observation layer. User is exposed to the system, its philosophy, and the transformation offered.
3. `offer.html` — Offer presentation. User sees the product or service (Academy), its content, and its value.

**At each page, the user either continues forward or exits.**

If the user exits: no action is taken. No follow-up is initiated automatically.

---

## STEP 3 — DECISION

**On `offer.html`, the user makes a binary decision:**

- **YES** → clicks the main CTA ("Sisenen Akadeemiasse" / Enter the Academy)
- **NO** → leaves the page

**If YES:** user is directed to the Gumroad checkout page at `aurinbeyond.gumroad.com`.

**Before proceeding, the user has access to:**

- `disclaimer.html` — liability disclaimer
- `client-agreement.html` — service agreement
- `pricing-policy.html` — currency and pricing policy (NOK base)

These documents are visible and linked. Reading them is the user's responsibility.

---

## STEP 4 — ACTION

**On Gumroad:**

The user reviews the product listing, price (in NOK), and proceeds to enter payment details.

- Email address is collected by Gumroad
- Payment method is entered (card or other supported method)
- User confirms the order

**At this point the client has acknowledged:**

- Base currency is NOK
- Displayed price is the final price
- Any bank conversion fees are their responsibility

---

## STEP 5 — PAYMENT

**Processing:**

- Payment is processed by Gumroad's system
- Transaction currency: NOK
- Gumroad handles all payment security and processing

**Two outcomes:**

- **Success** → user proceeds to Step 6
- **Failure** (declined card, insufficient funds, etc.) → user is returned to Gumroad checkout; no order is created

---

## STEP 6 — CONFIRMATION

**After successful payment:**

- Gumroad sends an automated order confirmation email to the user's email address
- The email includes: order ID, product name, amount charged, and access instructions

**On-site:**

- User may be redirected to `success.html`
- `success.html` confirms the activation and sets the tone for what follows

---

## STEP 7 — DELIVERY

**Digital product / service delivery:**

- Access link or content is delivered via Gumroad's system to the user's email
- Delivery is immediate upon payment confirmation
- No physical shipment occurs

**What is delivered:**

- Access to the purchased digital content (Academy modules, sessions, or materials)
- Any onboarding instructions specified in the product listing

**If delivery fails** (email not received):

- User contacts support
- Support verifies purchase via order ID and resends access

---

## STEP 8 — FOLLOW-UP

**Post-purchase:**

- No automated follow-up sequence is active unless explicitly configured
- User retains access to purchased content as defined in the product terms
- If the user has questions or issues, they contact support directly

**Ongoing access:**

- Content remains accessible per the terms defined at point of purchase
- Pure Soul Life reserves the right to update content within the same product

---

## STEP 9 — NEXT STEP

**The user is presented with a clear next action after completing the current product:**

- Inside the delivered content or via the confirmation email, a next-step offer or invitation is referenced
- This may be: an upsell to a higher-tier product, a 1:1 session booking, or re-engagement with new content
- The user acts on it or does not — no pressure sequence runs automatically

**See:** `OFFER-ARCHITECTURE.md` for the product ladder and next-step logic.

---

## SUPPORT CONTACT

At any point in the flow, the user can contact support before or after purchase.

Contact must be initiated by the user.
Pure Soul Life does not initiate unsolicited contact.

---

## FLOW SUMMARY TABLE

| Step | Location | User Action | System Response |
|------|----------|-------------|-----------------|
| 1. Entry | Social / Link | Clicks link | Lands on `index.html` |
| 2. Page | `index.html` → `vsl.html` → `offer.html` | Reads and navigates | Pages load in sequence |
| 3. Decision | `offer.html` | Clicks CTA or exits | Redirects to Gumroad |
| 4. Action | Gumroad | Fills payment details | Order form displayed |
| 5. Payment | Gumroad | Confirms purchase | Payment processed in NOK |
| 6. Confirmation | Email + `success.html` | Receives confirmation | Email sent by Gumroad |
| 7. Delivery | Email | Opens access link | Content delivered digitally |
| 8. Follow-up | Email / Support | Contacts support if needed | Support responds manually |
| 9. Next Step | Delivered content / Email | Reviews next-step offer | Next offer referenced in content |

---

STATUS: Active // Pure Soul Life // GENESIS Business Logic Layer
