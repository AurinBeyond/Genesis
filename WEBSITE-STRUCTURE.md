# WEBSITE STRUCTURE v1.0

**Task ID:** WEB-001
**Brand:** Aurin Beyond / Aurin OS
**Layer:** Frontend / User Experience / Positioning
**Status:** Active

---

## CORE PRINCIPLE

> If the user is confused, they leave. If the user understands, they stay.

---

## SITE PURPOSE

Answer four questions within the first 5 seconds:

1. What is this?
2. Is this for me?
3. What do I get?
4. What do I do next?

---

## NAVIGATION STRUCTURE

```
index.html          HOME            → Entry point. Core message. Main CTA.
vsl.html            OBSERVATION     → Depth layer. System philosophy. Bridge to offer.
offer.html          ACADEMY         → Product. What user gets. Purchase CTA.
success.html        CONFIRMED       → Post-purchase. Delivery instructions.
protocol.html       START           → First step. Entry into the system.
disclaimer.html     RESPONSIBILITY  → Legal clarity. Liability.
client-agreement.html  AGREEMENT    → Service terms.
pricing-policy.html    PRICING       → Currency and payment rules.
terms.html          TERMS           → Full terms of use.
contact (email)     CONTACT         → Single support channel.
```

---

## PAGE ARCHITECTURE

---

### PAGE 1 — HOME (`index.html`)

**Role:** First impression. Brand entry. Clear positioning.

**Structure:**
```
[NAV] → Avaleht / Vaatlus / Akadeemia / Vastutus
[HERO]
  VERSION LABEL: AURIN OS
  HEADLINE: Core message — pattern interruption
  SUBTEXT: 1 sentence — what this does
  CTA: "Alusta vaatlust" → vsl.html
[FOOTER] → disclaimer link
```

**User goal:** Understand what this is. Feel it is for them. Click forward.

**Connected to:** `vsl.html`, `disclaimer.html`

---

### PAGE 2 — OBSERVATION (`vsl.html`)

**Role:** Philosophy layer. System explanation. Pre-offer depth.

**Structure:**
```
[NAV]
[HERO]
  LABEL: SYSTEM AUDIT
  HEADLINE: See the pattern before it drives you.
  VIDEO PLACEHOLDER or Content block
[3-CARD GRID]
  Card 1: Detection — repeating cycles
  Card 2: Analysis — where the pattern formed
  Card 3: Choice — pause between reaction and action
[CTA] → offer.html
[FOOTER]
```

**User goal:** Understand the system's logic. Build enough trust to proceed.

**Connected to:** `index.html` (back), `offer.html` (forward)

---

### PAGE 3 — ACADEMY / OFFER (`offer.html`)

**Role:** Product presentation. Value statement. Purchase CTA.

**Structure:**
```
[NAV]
[HEADER]
  EYEBROW: Stage 03: Integration
  HEADLINE: Genesis Program
  SUBTEXT: Entry to the architect level begins here.
[PRODUCT PANEL]
  Features list (4 items)
  Price in NOK
  CTA: "Sisenen Akadeemiasse" → Gumroad
[CONTEXT BLOCK]
  What to expect after entry
[FOOTER LEGAL LINKS]
  disclaimer / client-agreement
```

**User goal:** Evaluate the offer. Decide. Click to Gumroad.

**Connected to:** `vsl.html` (back), `https://aurinbeyond.gumroad.com/l/[slug]` (forward), `disclaimer.html`, `client-agreement.html`

---

### PAGE 4 — CONFIRMATION (`success.html`)

**Role:** Post-purchase landing. Confirm delivery. Set next step.

**Structure:**
```
[CONFIRMATION MESSAGE]
  Purchase confirmed.
  Check email for access.
[NAVIGATION CARDS]
  → protocol.html (24h protocol)
  → notes.html (notes space)
  → void.html (observation layer)
[BACK TO HUB] → index.html
[SUPPORT] → contact.puresoul@proton.me
[FOOTER]
```

**User goal:** Feel confirmed. Know what to do next. Have support access.

**Connected to:** `protocol.html`, `notes.html`, `index.html`

---

### PAGE 5 — START / PROTOCOL (`protocol.html`)

**Role:** First action step inside the system.

**Structure:**
```
[HEADER]
  LABEL: PROTOCOL
  HEADLINE: 24h Observation Protocol
[PROTOCOL STEPS]
  Step-by-step structured instructions
[NAVIGATION]
  Back / Forward
[FOOTER]
```

**User goal:** Begin. Execute the first protocol. Have a clear path.

**Connected to:** `success.html` (back), continuation path forward

---

### PAGE 6 — LEGAL PAGES

**Role:** Transparency. User responsibility. Trust infrastructure.

**Files:**
- `disclaimer.html` — liability disclaimer
- `client-agreement.html` — service agreement
- `pricing-policy.html` — NOK pricing rules
- `terms.html` — full terms of use
- `legal.html` — legal hub / index

**Structure (each page):**
```
[BACK LINK] → offer.html
[DOCUMENT TITLE]
[DOCUMENT CONTENT]
[FOOTER]
```

**User goal:** Read and understand before purchase. Find answer to specific legal question.

**Connected to:** `offer.html` footer links, `disclaimer.html`, `client-agreement.html`

---

### PAGE 7 — CONTACT

**Format:** Email only. No contact form on site.

**Address:** `contact.puresoul@proton.me`

**Where it appears:**
- `success.html` — post-purchase support
- `disclaimer.html` — legal questions
- `client-agreement.html` — agreement questions
- `DELIVERY-SYSTEM.md` — delivery failures

**Policy:** User initiates. No unsolicited contact from Pure Soul Life.

---

## FULL NAVIGATION MAP

```
HOME (index.html)
  │
  └─→ OBSERVATION (vsl.html)
         │
         └─→ ACADEMY (offer.html)
                │
                ├─→ GUMROAD (external — checkout)
                │      │
                │      └─→ SUCCESS (success.html)
                │              │
                │              ├─→ PROTOCOL (protocol.html)
                │              ├─→ NOTES (notes.html)
                │              └─→ HOME (index.html)
                │
                ├─→ DISCLAIMER (disclaimer.html)
                ├─→ CLIENT AGREEMENT (client-agreement.html)
                └─→ PRICING POLICY (pricing-policy.html)

ARKANA-OS FLOW (separate layer):
  HOME → VOID (void.html) → CORE (core.html) → DELTA (delta.insight.html)
  → SIGMA CORE (sigma.core.html) → SIGMA PROTOCOL (sigma-protocol.html)
```

---

## SYSTEM CONNECTIONS

| Site Component | External System | Connection |
|----------------|----------------|-----------|
| `offer.html` CTA | Gumroad | Direct link to product listing |
| `success.html` | Gumroad delivery email | Confirmation alignment |
| Distribution posts | `index.html` | Bio link in social profile |
| `ENTRY-POINT.md` | `index.html` | Core message mirrored |
| `USER-FLOW.md` | Site flow | Steps 1–3 are site pages |
| `DELIVERY-SYSTEM.md` | Gumroad email | Steps 4–9 are post-site |

---

## VALIDATION CHECKLIST

- [ ] User understands site purpose in under 5 seconds
- [ ] CTA is visible and clear on every page
- [ ] Legal documents are linked and accessible before purchase
- [ ] Navigation chain has no dead ends
- [ ] Support contact is reachable from post-purchase pages
- [ ] No page requires scrolling to find the primary action

---

STATUS: Active // Pure Soul Life / Aurin Beyond // GENESIS Frontend Layer
