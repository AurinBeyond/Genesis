# OFFER ARCHITECTURE v1.0

**Brand:** Pure Soul Life
**Task ID:** FLOW-CORE-001
**Layer:** Business Execution
**Status:** Active

---

## REVENUE STRUCTURE

Pure Soul Life operates a single-tier digital product system with a defined upsell path.

```
ENTRY PRODUCT → CORE PRODUCT → HIGH-TOUCH OFFER
```

Each level is independent. A client can enter at any level.

---

## I. PRODUCT LADDER

### Level 1 — Entry Product

**Format:** Digital content (PDF, audio, short module)

**Purpose:** First point of transaction. Demonstrates value at low commitment.

**Price range:** Low (accessible to a wide audience)

**Delivery:** Immediate via Gumroad

**Next step presented:** Link or reference to Level 2 inside the delivered content

---

### Level 2 — Core Product (Academy)

**Format:** Full digital program or Academy access

**Purpose:** The primary revenue product. Delivers the complete system.

**Access point:** `offer.html` → Gumroad → `aurinbeyond.gumroad.com`

**Price:** Defined in NOK on the Gumroad listing

**Delivery:** Immediate digital access via Gumroad

**Next step presented:** Reference to Level 3 inside the content or confirmation email

---

### Level 3 — High-Touch Offer

**Format:** 1:1 session or direct consultation

**Purpose:** Personal engagement at premium price point

**Access:** Booking via direct contact or dedicated link (not publicly listed on main offer page by default)

**Price:** Highest tier. Defined per session or package.

**Delivery:** Session is confirmed manually within 24 hours

---

## II. REVENUE LOGIC

| Level | Volume | Price | Revenue Contribution |
|-------|--------|-------|---------------------|
| 1 — Entry | High | Low | Acquisition / list-building |
| 2 — Core | Medium | Mid | Primary revenue engine |
| 3 — High-Touch | Low | High | Premium margin |

The system does not require all three levels to operate. Level 2 alone is a complete business unit.

---

## III. PRICING RULES

- All prices are denominated in NOK
- Prices are set in the Gumroad listing and are the single source of truth
- Prices are not negotiated via email or social
- No discount codes are active unless explicitly configured
- Currency conversion is an estimate only — see `laws/PRICING-CURRENCY-POLICY.md`

---

## IV. OFFER PRESENTATION

The offer is presented on one page: `offer.html`

`offer.html` contains:
- What the product is
- What it delivers
- Single CTA: "Sisenen Akadeemiasse" → Gumroad

No upsell is shown at the `offer.html` level. The next-step offer is embedded inside the delivered product.

---

## V. WHAT DOES NOT EXIST

- Bundles combining multiple products at checkout
- Free trials or preview access
- Subscription billing (all purchases are one-time)
- Affiliate or referral programs

These may be added in a future version. They are not active now.

---

## VI. NEXT STEP TRIGGER

After each purchase, the next-step offer is communicated inside the product content.

| Current Product | Next Step Offered |
|----------------|------------------|
| Level 1 — Entry | Reference to Level 2 (Academy) |
| Level 2 — Academy | Reference to Level 3 (1:1 session) |
| Level 3 — 1:1 | No automatic next step; handled manually |

The client is never pushed. The next step is presented once, clearly.

---

## LINKED DOCUMENTS

- `USER-FLOW.md` — full client journey
- `DELIVERY-SYSTEM.md` — how each product is delivered
- `CLIENT-COMMUNICATION.md` — how next steps are communicated

---

STATUS: Active // Pure Soul Life // GENESIS Business Execution Layer
