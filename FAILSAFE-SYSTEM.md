# FAILSAFE SYSTEM v1.0

**Task ID:** FAILSAFE-001
**Brand:** Pure Soul Life
**Layer:** Stability / Support / Trust
**Status:** Active

---

## PURPOSE

Define a complete recovery path for every critical failure point in the system.

No user is left stuck, confused, or without a next step.

```
FAILURE → DETECTION → RESPONSE → RESOLUTION
```

---

## CONNECTED DOCUMENTS

| Document | Role |
|----------|------|
| `laws/DELIVERY-ACCESS-POLICY.md` | Governs delivery responsibility and access rights |
| `CLIENT-COMMUNICATION.md` | Support tone, response time, scope |
| `AUTOMATION-FLOW.md` | Defines what is manual vs automated; escalation paths |
| `USER-FLOW.md` | Full user journey; failure points map to this flow |
| `laws/PRICING-CURRENCY-POLICY.md` | Currency and receipt reference for payment confusion |

---

## FAILURE AREA 1 — DELIVERY FAILURE

### Scenarios covered

| # | Scenario |
|---|----------|
| 1a | Email not received after purchase |
| 1b | Email delivered to spam / junk folder |
| 1c | Wrong email address entered at checkout |
| 1d | Gumroad email delayed beyond 15 minutes |

---

### User instructions (shown on `success.html` and in listing)

> **Did not receive your email?**
>
> 1. Check your spam or junk folder. Gumroad emails are automated and are sometimes filtered.
> 2. Wait up to 15 minutes from purchase time before taking action.
> 3. If still not received after 15 minutes: email `contact.puresoul@proton.me` with your order ID and the email address used at checkout.

---

### System response

| Scenario | Action |
|----------|--------|
| 1a — email not received | Support verifies order in Gumroad; resends download link manually |
| 1b — spam folder | User self-resolves; support confirms if needed |
| 1c — wrong email | Support verifies order by order ID; resends to correct email upon request |
| 1d — platform delay | Support monitors; resends after confirming Gumroad delivery status |

**Response time:** Within 24 hours of support contact.

**What support sends:**
- Confirmation that order exists in system
- Direct download link (Gumroad resend function)
- One-line note on next step

**Recovery outcome:** User receives PDF download link. No purchase is lost.

---

## FAILURE AREA 2 — ACCESS FAILURE

### Scenarios covered

| # | Scenario |
|---|----------|
| 2a | Download link not working (expired or broken) |
| 2b | Page not loading (`success.html`, module page) |
| 2c | Client cannot open the PDF file |
| 2d | Gumroad access page returns error |

---

### User instructions

> **Link not working or page not loading?**
>
> 1. Try opening the link in a different browser or device.
> 2. If the download link has expired: email `contact.puresoul@proton.me` with your order ID. A fresh link will be sent.
> 3. If a page is not loading: this is a temporary platform issue. Wait 15 minutes and try again. If it persists, contact support.

---

### System response

| Scenario | Action |
|----------|--------|
| 2a — expired/broken link | Support uses Gumroad admin to resend fresh download link |
| 2b — page not loading | Temporary issue; support confirms and provides direct link if needed |
| 2c — cannot open PDF | Support confirms file format and provides alternative format if possible |
| 2d — Gumroad error | Support monitors Gumroad status; notifies client of delay with ETA |

**Response time:** Within 24 hours.

**Recovery outcome:** User receives a working download link or clear confirmation of when access will be restored.

---

## FAILURE AREA 3 — PAYMENT CONFUSION

### Scenarios covered

| # | Scenario |
|---|----------|
| 3a | User unsure whether payment succeeded |
| 3b | Charged amount differs from displayed price |
| 3c | Currency confusion (expected local currency, charged in NOK) |
| 3d | Double charge (rare — Gumroad-level issue) |

---

### User instructions

> **Unsure if payment went through?**
>
> 1. Check the email address used at checkout. Gumroad sends an order confirmation immediately after a successful payment.
> 2. Check your bank statement for a charge in NOK (Norwegian Kroner). All Pure Soul Life transactions are processed in NOK.
> 3. If you were charged but received no confirmation email: email `contact.puresoul@proton.me` with your order ID or a screenshot of the bank charge.
> 4. If the amount appears different from what you expected: see the Pricing & Currency Policy. All prices are in NOK. Displayed local currency amounts are estimates.

---

### System response

| Scenario | Action |
|----------|--------|
| 3a — uncertain payment | Support checks Gumroad order history by email; confirms payment status |
| 3b — amount mismatch | Support references `laws/PRICING-CURRENCY-POLICY.md`; explains NOK base + conversion |
| 3c — currency confusion | Support sends clear explanation of NOK billing; no refund issued for currency misunderstanding (policy applies) |
| 3d — double charge | Support escalates to Gumroad support immediately; coordinates refund if confirmed |

**Response time:** Within 24 hours. Double charges escalated immediately.

**Recovery outcome:** User has confirmed payment status. Currency confusion is resolved with documentation. Double charges are escalated to Gumroad within 24 hours.

---

## FAILURE AREA 4 — USER CONFUSION (POST-PURCHASE)

### Scenarios covered

| # | Scenario |
|---|----------|
| 4a | User does not know what to do after buying |
| 4b | User feels lost after receiving the PDF |
| 4c | User unsure what the product is or what it delivers |
| 4d | User asks "what's next?" with no clear answer in sight |

---

### Primary resolution — post-purchase page

`success.html` provides:
- Confirmation that the purchase is active
- Instruction to check email for delivery
- A single clear next action

No confusion should remain after reading `success.html`. If it does, the page should be updated.

---

### User instructions (support response template)

> **Not sure what to do next?**
>
> You purchased: *[Product Name]*.
>
> Here is your next step:
>
> 1. Open the email you used at checkout. Your download link is there.
> 2. Click the link and download the PDF.
> 3. Read it from start to finish. It is short. It is designed to be read once, then applied.
> 4. The last page tells you what comes after this.
>
> If you have a question after reading: email `contact.puresoul@proton.me`.

---

### System response

| Scenario | Action |
|----------|--------|
| 4a — lost after purchase | Support sends post-purchase orientation message (template above) |
| 4b — lost after PDF | Support clarifies product scope; directs to next step inside PDF |
| 4c — confused about product | Support restates what was purchased and what it delivers |
| 4d — no visible next step | Support references next-step line from PDF; links to offer page if appropriate |

**Tone:** Calm. Direct. One step at a time. No performance of enthusiasm.

**Recovery outcome:** User has a single clear next action. System does not end in silence.

---

## FAILURE AREA 5 — TECHNICAL FAILURE

### Scenarios covered

| # | Scenario |
|---|----------|
| 5a | Gumroad platform delay or downtime |
| 5b | Email delivery delayed by mail system |
| 5c | Site pages temporarily unavailable |
| 5d | Support inbox delayed (inbox not checked same day) |

---

### Expected wait times

| Failure | Expected Wait | When to Act |
|---------|--------------|-------------|
| Gumroad email delay | Up to 15 min | Contact support if not received after 15 min |
| Mail system delay | Up to 30 min | Contact support after 30 min if still nothing |
| Site page not loading | Up to 15 min | Contact support if still down after 15 min |
| Support response | Up to 24 hours | If no reply after 24 hours, resend the email |

---

### User instructions

> **Something seems delayed?**
>
> 1. Wait the time shown above before taking action. Most delays are brief and self-resolve.
> 2. If the wait time passes and nothing has changed: email `contact.puresoul@proton.me` with a description of the issue and your order ID.
> 3. You will receive a response within 24 hours.
> 4. Your purchase is secure. A platform delay does not affect your order.

---

### System response

| Scenario | Action |
|----------|--------|
| 5a — Gumroad downtime | Monitor Gumroad status page; notify affected clients if downtime > 2 hours |
| 5b — email delay | Confirm order exists; resend manually if delay confirmed |
| 5c — site pages down | Restore pages or provide direct download link via email |
| 5d — support inbox delay | Support checks inbox minimum once per business day (per `AUTOMATION-FLOW.md`) |

**Recovery outcome:** No technical failure is invisible. Every failure has a defined wait time and a defined action after that window passes.

---

## FAILURE AREA 6 — SUPPORT SYSTEM

### Contact method

| Channel | Address |
|---------|---------|
| Email | `contact.puresoul@proton.me` |

No other support channel is active. No phone. No chat. No social DMs.

---

### What to include in support email

Client must provide:
1. Order ID (from Gumroad confirmation email)
2. Email address used at checkout
3. Description of the issue (one sentence is enough)

If order ID is not available: name and email address are sufficient to locate the order.

---

### Response time

| Request type | Response time |
|-------------|--------------|
| Delivery failure / access issue | Within 24 hours |
| Payment confirmation | Within 24 hours |
| General question | Within 24 hours |
| Refund request | Within 48 hours (reviewed against refund policy) |
| Double charge (urgent) | Escalated immediately |

---

### Support tone

- Calm. No defensiveness.
- Direct. One instruction at a time.
- No unsolicited advice.
- No emotional performance.
- Respond in the language the client used.
- If the issue is outside scope: state that clearly and direct to the correct channel.

Per `CLIENT-COMMUNICATION.md` — Section: Touchpoint 3.

---

### What support will NOT do

- Promise refunds not covered by policy
- Issue credits or compensation not defined in policy
- Engage in extended back-and-forth without resolution
- Leave a message unanswered

---

## FAILSAFE VALIDATION

| Failure Area | Every scenario has a response? | User always has a next step? | No scenario ends in silence? |
|-------------|-------------------------------|------------------------------|------------------------------|
| Delivery Failure | ✅ Yes | ✅ Yes | ✅ Yes |
| Access Failure | ✅ Yes | ✅ Yes | ✅ Yes |
| Payment Confusion | ✅ Yes | ✅ Yes | ✅ Yes |
| User Confusion | ✅ Yes | ✅ Yes | ✅ Yes |
| Technical Failure | ✅ Yes | ✅ Yes | ✅ Yes |
| Support System | ✅ Yes | ✅ Yes | ✅ Yes |

---

## CORE PRINCIPLE

> A system is not tested when it works.
> A system is proven when it fails — and recovers.

Every failure in this system has a defined response. No user is blocked. No scenario ends without a next step.

---

STATUS: Active // Pure Soul Life // GENESIS Stability Layer
