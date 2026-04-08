# COURSE-001: COURSE DELIVERY & USER SPACE SYSTEM

**Task ID:** COURSE-001
**Brand:** Pure Soul Life
**Layer:** Delivery / Experience
**Status:** Active

---

## CORE PRINCIPLE

> Structured access. Personal pace. Clear progression.

---

## 1. COURSE STRUCTURE

A course is divided into sequential modules. Each module is one unit of content.

**Module format:**

| Component | Description |
|-----------|-------------|
| Content | Written text page (HTML page or PDF) and/or video/audio link |
| Exercise | One practical task tied to the module topic |
| Reflection (optional) | One open-ended question the client answers for themselves |

**Example structure (7-day course):**

| Module | Title | Content |
|--------|-------|---------|
| Module 1 | The Source Within | `01-the-source-within.md` |
| Module 2 | Perception Break | `02-perception-break.md` |
| Module 3 | Identity Deconstruction | `03-identity-deconstruction.md` |
| Module 4 | System Detachment | `04-system-detachment.md` |
| Module 5 | Internal Authority | `05-internal-authority.md` |
| Module 6 | Reality Reconstruction | `06-reality-reconstruction.md` |
| Module 7 | Integration | `07-integration.md` |

> Content source files exist in the repository root. Each module maps directly to one source file.

---

## 2. ACCESS LOGIC

### Unlock Method: Email-Based Sequential Unlock (Manual Trigger)

**One method only. No mixed logic.**

| Why email-based? |
|-----------------|
| No LMS platform required |
| Works with Gumroad + basic site pages |
| Fully operable with existing tools |
| Manually resendable in case of failure |

### Sequence

```
PURCHASE → Module 1 link sent immediately (Gumroad delivery email)
↓
Client completes Module 1
↓
Client clicks "I've completed this module" link at the bottom of the module page
  → sends notification to support email (contact.puresoul@proton.me)
↓
Support sends Module 2 link within 24 hours
↓
Repeat for each subsequent module
```

### Rules

- Module 1 is accessible **immediately** after purchase (delivered via Gumroad email)
- Modules 2–7 are unlocked **one at a time** via email, triggered by client completion signal
- No module is skipped
- No time-based auto-unlock — client sets the pace
- If client does not signal completion: they remain on current module. No forced progression.

### Completion Signal

Each module page includes a single link at the bottom:

> **"I have completed this module → continue to the next"**

This link sends an email to `contact.puresoul@proton.me` with subject line:
`[COURSE] [Client Name or Email] completed Module X`

Support processes this within 24 hours and sends the next module link.

---

## 3. PERSONAL USER SPACE

Each client receives a **Personal Access Page** — a hidden, unlisted HTML page with a unique URL.

### Structure

```
/client-space/[unique-id].html
```

Example: `/client-space/abc123.html`

The URL is not indexed and is not publicly listed. It is delivered to the client in their purchase confirmation email and re-sent upon request.

### Page Content

```
Pure Soul Life — Your Course Space
────────────────────────────────────

Welcome, [Client First Name].
This is your personal access page. All your modules are listed below.

────────────────────────────────────
MODULE 1 — The Source Within          [OPEN →]
MODULE 2 — Perception Break           [LOCKED]
MODULE 3 — Identity Deconstruction    [LOCKED]
MODULE 4 — System Detachment          [LOCKED]
MODULE 5 — Internal Authority         [LOCKED]
MODULE 6 — Reality Reconstruction     [LOCKED]
MODULE 7 — Integration                [LOCKED]
────────────────────────────────────

Need help? contact.puresoul@proton.me — include your order ID.
```

### Access Logic on the Page

- **Unlocked module** → displayed as a clickable link to that module's page
- **Locked module** → displayed as plain text with `[LOCKED]` label
- The page is **static HTML** — no database, no login, no account required
- When a module is unlocked, support updates the client's personal page (replaces `[LOCKED]` with the module link)

### Page Update Process

When a client completes a module and support sends the next link:
1. Support opens `client-space/[unique-id].html`
2. Changes `MODULE X — [Title]  [LOCKED]` → `MODULE X — [Title]  [OPEN →]` with the module link
3. Saves the file
4. Sends the client the direct link to that module in an email

---

## 4. PROGRESS MODEL

| Rule | Value |
|------|-------|
| Pace | Client-controlled — no time pressure |
| Minimum speed | None — client can take days or weeks per module |
| Maximum speed | One module per 24 hours (support response window) |
| Skipping | Not permitted — sequential only |
| Returning | Client uses their personal access page URL at any time |

**Principle:** Access is structured. Speed is personal.

The client's personal page is their permanent reference point. They can return to it at any time using the URL in their original purchase email.

---

## 5. DELIVERY CONNECTION

| System | Connection |
|--------|-----------|
| `DELIVERY-SYSTEM.md` | Module 1 is part of the initial Gumroad delivery. Subsequent modules follow the email-based delivery path |
| `AUTOMATION-FLOW.md` | Module unlock is manual — listed under "What Is Done Manually" (support trigger within 24 hours) |
| `USER-FLOW.md` | Post-purchase step: client receives Module 1 link + personal access page URL |
| `CLIENT-COMMUNICATION.md` | Module delivery emails follow the established communication standard |
| `laws/DELIVERY-ACCESS-POLICY.md` | Governs access rights, resend policy, and responsibility boundaries |

---

## 6. CLIENT EXPERIENCE

### Step 1 — After Purchase

Client receives a Gumroad confirmation email containing:
- Order ID
- Link to **Module 1**
- Link to their **Personal Access Page**
- Support email for any questions

### Step 2 — Module 1

Client opens Module 1. They read, work through the exercise, and answer the optional reflection.

At the bottom of the page:
> **"I have completed this module → signal completion"** *(mailto link to support)*

### Step 3 — Module Unlock

Support receives the completion signal and sends Module 2 link within 24 hours.
Support also updates the client's personal access page to show Module 2 as unlocked.

### Step 4 — Ongoing Access

Client returns to their personal access page at any time using the URL from their original email. The page always shows their current state: which modules are open, which are locked.

### Step 5 — Final Module

After completing Module 7, the client receives:
- A completion confirmation email
- A reference to the next step in the system (Level 2 — Academy or Level 3 — 1:1 session)

### What the Client Always Knows

| Question | Answer |
|----------|--------|
| Where am I? | Personal access page shows current open modules |
| What is next? | Next locked module is visible, awaiting unlock |
| How do I continue? | Signal completion via the link at the bottom of the current module |
| Where do I go back? | Personal access page URL (in original purchase email) |

---

## 7. FAILSAFE LOGIC

| Failure | Detection | Resolution |
|---------|-----------|------------|
| Client did not receive purchase email | Client reports it | Support verifies order in Gumroad, manually resends Module 1 link and personal page URL |
| Client lost personal access page URL | Client contacts support with order ID | Support resends URL within 24 hours |
| Completion signal email not received | Client follows up after 24 hours | Support manually checks and sends next module link |
| Module page link broken | Client reports it | Support resends corrected link within 24 hours |
| Client is inactive for extended period | No automatic action | Client resumes at any time; their page remains active |

**Support contact for all failures:** `contact.puresoul@proton.me`
**Required information:** Order ID (from original purchase email)

---

## 8. VALIDATION

| Requirement | Status |
|-------------|--------|
| No broken access points | ✅ Failsafe covers all failure modes |
| No duplicate content | ✅ One page per module, one personal page per client |
| No unclear navigation | ✅ Personal access page is single source of truth |
| No missing modules | ✅ All 7 modules defined and mapped to source files |
| No complex LMS | ✅ Static HTML pages + email only |
| No multiple access paths | ✅ Single path: personal page URL |
| No unclear unlock logic | ✅ One method: email-based manual trigger |
| Client can start immediately | ✅ Module 1 delivered via Gumroad on purchase |
| Client can continue anytime | ✅ Personal access page is permanent |
| Client can clearly navigate | ✅ Locked/unlocked state visible on personal page |

---

## 9. IMPLEMENTATION CHECKLIST

Before first client is enrolled:

- [ ] Module pages created (one HTML page per module, based on source `.md` files)
- [ ] Personal access page template created (`client-space/template.html`)
- [ ] Completion signal mailto links added to bottom of each module page (except Module 7)
- [ ] Gumroad purchase confirmation message updated to include personal access page URL
- [ ] Support inbox monitored for completion signals
- [ ] Process documented in `AUTOMATION-FLOW.md` (manual section updated)

---

STATUS: Active // Pure Soul Life // GENESIS Delivery Layer
