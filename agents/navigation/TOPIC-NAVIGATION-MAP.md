# TOPIC-NAVIGATION-MAP
# Agent Type: NAVIGATION AGENT
# Platform: AurinBeyond
# Version: 2.0
# Status: PRODUCTION

---

## 1. PURPOSE

### What this system is

This file defines the deterministic movement of users through the AurinBeyond platform.

It controls:
- how users enter the system
- which path they are assigned to
- what they encounter at each stage
- when and how free content connects to paid offers
- which transitions are permitted and which are forbidden

### Why it exists

Without structured routing, users encounter:
- conflicting content signals
- choice overload
- path collisions between incompatible audiences
- conversion friction created by premature offers
- brand signal dilution from topic mixing

This system eliminates those failure conditions.

### What it stabilizes

- Each topic path is self-contained
- Each stage has one defined next step
- Offers appear only after trust has been established
- Children content is isolated from conversion flows
- The main funnel remains dominant at all times

### Why topic-based routing is required

The platform serves users across multiple intent categories. A user seeking inner awakening content operates under different conditions than a user seeking structured learning or a parent looking for children's audio.

Routing by topic ensures:
- content relevance at each stage
- appropriate offer timing
- no audience contamination
- testable, measurable path performance

---

## 2. NAVIGATION PRINCIPLES

These rules are non-negotiable. All agents and systems must enforce them.

### P-01: One topic → one primary path
A user who enters through a topic is assigned to that topic's path. They do not see routing options from other topics until their current path is complete or explicitly exited.

### P-02: No excessive branching
Each stage of a path has exactly one primary next step. A soft alternative is permitted but must not compete with the primary step visually or structurally.

### P-03: Every free content piece must lead to a defined next step
Free content does not terminate. Every article, audio, or video leads to either:
- the next free content piece in the path, OR
- the trust-building step, OR
- the offer step (only after trust is established)

### P-04: Children content is isolated
Angel Tales content (children's domain) must never:
- feed into adult conversion flows
- display aggressive calls to action
- link to awakening, meditation, or course content
- be positioned within the main brand funnel

Angel Tales has its own soft path. Its offer is a gentle product presentation, not a funnel.

### P-05: The main funnel is dominant
The index → offer → success → protocol → continuation flow is the primary system. All topic branches support this funnel. None replace it.

### P-06: Offer only after trust is established
No offer appears on the entry page or the free value step. The offer step is only accessible after the user has passed through the trust-building step.

### P-07: Post-offer step is always defined
Whether the user accepts or declines the offer, they have a defined next destination. No dead ends.

### P-08: No cross-audience content mixing
Spiritual / awakening content must not share a page or step with children's content, course catalog pages, or service booking pages.

---

## 3. TOPIC BRANCHES

---

### TOPIC 1: AWAKENING / MATRIX / INNER AUTHORITY

**User intent:** Understand why life feels controlled, scripted, or disconnected from self. Seek clarity on identity, conditioning, and internal authority.

**Entry point:** `/awakening` — article or video addressing the gap between external noise and internal knowing.

**Free value step:** A single foundational article or short video. Subject: how conditioning creates the experience of being controlled. No offer. No product mention.

**Trust-building step:** `/vaatlus/awakening` — Awareness Page (Vaatlus). Deeper framing of the topic. Defines the problem clearly without providing a full solution. Ends with a single directional prompt: "There is a next step."

**Offer step:** `/offer/awakening` — Presents the product relevant to this topic (mini-course, eBook, or audio on inner authority / awakening from conditioning). One product only. One call to action. No alternatives presented.

**Post-offer step:**
- If accepted → `/success` → `/protocol` (24-hour onboarding sequence) → `/continuation/awakening`
- If declined → Soft redirect to free content deep-dive article. No re-offer on the same session.

**Soft alternative path:** Secondary article series accessible from the trust-building step sidebar. No offer links in the alternative path.

**Forbidden paths:**
- Entry page must NOT display product links
- Free value step must NOT display offer CTAs
- This path must NOT link to children content, course catalog, or services booking
- Re-offer must NOT appear within the same session after a decline
- Cross-links to other topic branches are NOT permitted from entry or free value steps

---

### TOPIC 2: MEDITATIONS / AFFIRMATIONS

**User intent:** Access structured audio or practice tools for internal state management. May be spiritually inclined or seeking practical tools without ideological framing.

**Entry point:** `/meditations` — Landing page listing available free meditation or affirmation audio. No offer presented here.

**Free value step:** One free audio (meditation or affirmation). Accessible without registration. Ends with a prompt: "More available in the full collection."

**Trust-building step:** `/vaatlus/meditations` — Awareness Page. Explains how consistent audio practice affects internal state over time. Frames the collection as a structured system, not a random library.

**Offer step:** `/offer/meditations` — Presents the full audio collection or meditation program. One product. Single call to action.

**Post-offer step:**
- If accepted → `/success` → `/protocol` → `/continuation/meditations`
- If declined → Return to free audio library with no further offer prompts in that session.

**Soft alternative path:** Additional free audio (one item). Accessible from the trust-building step. No offer link embedded.

**Forbidden paths:**
- Free audio must NOT be gated behind registration without clear user agreement
- Offer must NOT appear before trust-building step is complete
- Meditation path must NOT link into awakening funnel or course catalog during active path progression
- This path must NOT feed into children content

---

### TOPIC 3: CHILDREN CONTENT (ANGEL TALES)

**User intent:** Parent or guardian seeking audio, stories, or content for children focused on positive values, calm, or imagination.

**Entry point:** `/angel-tales` — Dedicated children's content page. Visually and tonally distinct from all other platform content.

**Free value step:** One free story or audio episode. No registration required. Calm, non-commercial presentation.

**Trust-building step:** `/angel-tales/about` — Describes the purpose and design of Angel Tales. No platform brand integration. No awakening, meditation, or adult content references.

**Offer step:** `/angel-tales/collection` — Presents the full Angel Tales audio collection or story pack. Soft, non-aggressive presentation. No countdown timers, urgency language, or social proof pressure tactics.

**Post-offer step:**
- If accepted → Simple download or access confirmation. No protocol. No continuation sequence beyond a thank-you note and content access.
- If declined → Return to the free episode page. No further prompts.

**Soft alternative path:** Preview of second free episode. Accessible from the about page.

**Forbidden paths:**
- Angel Tales must NOT display any AurinBeyond main funnel CTAs
- Angel Tales must NOT link to awakening, meditation, or course content
- Angel Tales must NOT appear in the main navigation funnel
- No urgency language, countdown timers, or scarcity framing anywhere in this path
- No email capture requirement before accessing the free content

---

### TOPIC 4: COURSES / LEARNING PROGRAMS

**User intent:** Structured, sequential learning. User is ready to commit time and attention to a defined curriculum. Goal-oriented. May not have entered through the awakening or meditation paths.

**Entry point:** `/courses` — Course catalog page. Lists available learning programs with clear descriptions, duration, and outcome statements. No emotional persuasion language.

**Free value step:** One free module or introductory lesson from the course. Full access, no registration required.

**Trust-building step:** `/vaatlus/courses` — Awareness Page. Frames what the course system is designed to produce. Distinguishes AurinBeyond courses from standard self-help programs. Does not use testimonials or social proof as primary trust mechanism.

**Offer step:** `/offer/courses/[course-slug]` — Individual course purchase page. One course at a time. No upsell bundles presented on the same page.

**Post-offer step:**
- If accepted → Course onboarding sequence. Access confirmed. Welcome message. First module instruction.
- If declined → Return to course catalog. No re-offer pop-ups or exit-intent captures.

**Soft alternative path:** Related free article from the awakening or meditations branch. Accessible from the trust-building step only. No offer links embedded in cross-topic referral.

**Forbidden paths:**
- Course catalog must NOT display price before course description
- No upsell or cross-sell on the offer or post-offer page
- Courses path must NOT link to services booking during active path progression
- No auto-enrollment or pre-checked purchase options

---

### TOPIC 5: SERVICES / SESSIONS

**User intent:** Direct interaction with the AurinBeyond system or practitioner. High intent. May have completed a course or awakening path. Seeking personalized engagement.

**Entry point:** `/services` — Services overview page. Describes available sessions or offerings. Clear format, duration, and scope for each.

**Free value step:** Introductory description of what a session involves. What happens before, during, and after. No sales language. Sets expectations only.

**Trust-building step:** `/vaatlus/services` — Awareness Page. Frames the purpose and design philosophy behind the sessions. Aligns with the brand's "Source is internal" principle — sessions are a system, not a dependency.

**Offer step:** `/offer/services/[service-slug]` — Booking page for a specific service. Calendar or contact form. Single option presented. No package comparisons on the booking page.

**Post-offer step:**
- If booked → Confirmation page with session preparation instructions. No upsell.
- If not booked → Return to services overview. No follow-up automation triggered in the same session.

**Soft alternative path:** Recommendation to complete a relevant course first, if user has not done so. Non-pressured. One clear link. No forced redirect.

**Forbidden paths:**
- Services path must NOT display testimonials as the primary trust mechanism
- No discounts or urgency language on the booking page
- Sessions must NOT be framed as a dependency or ongoing requirement
- Services path must NOT be accessible as an entry point from children's content
- No auto-booking or pre-filled booking forms without explicit user action

---

## 4. CROSS-PATH RULES

### When cross-topic movement is permitted

A user may be directed to another topic path ONLY under these conditions:

1. The user has completed the post-offer step of their current path (accepted or declined)
2. The user has explicitly exited their current path via a defined exit point
3. A cross-topic recommendation appears ONLY in the post-offer or continuation stage, not before

### When cross-topic movement is restricted

Cross-topic movement is BLOCKED:
- During entry, free value, or trust-building stages
- When topics serve incompatible audiences (e.g., children's content and awakening content must never cross-link)
- When the user has not yet completed the trust-building step of their current path

### Incompatible audience pairs — never cross-link under any condition

| Topic A | Topic B | Reason |
|---|---|---|
| Angel Tales | Awakening / Matrix | Different audience, different tone |
| Angel Tales | Meditations (adult) | Content designed for different developmental stage |
| Angel Tales | Services / Sessions | Adult engagement format |
| Angel Tales | Courses | Different age and intent context |

### Cognitive load rule

No stage in any path may present more than two options:
- Primary next step (required)
- Soft alternative (optional, visually secondary)

Three or more options on a single stage page is a routing failure.

---

## 5. FUNNEL INTEGRITY RULES

### Primary funnel definition

`index → offer → success → protocol → continuation`

This is the main system spine. It takes precedence over all topic branches.

### Side paths definition

All five topic branches are side paths. They feed into the primary funnel at the offer step.

### Redirect rules

| Condition | Action |
|---|---|
| User reaches a dead-end page (no next step defined) | Redirect to topic entry page |
| User declines offer | Redirect to soft alternative path within same topic |
| User completes a topic path | Offer a single cross-topic recommendation or return to index |
| User lands on `/offer` without completing trust-building step | Redirect to trust-building step |
| User navigates directly to `/success` or `/protocol` without completing offer step | Redirect to index |

### Broken flow conditions

A flow is considered broken when:
- A page exists with no defined outbound path
- A user can access an offer page without passing through a trust-building step
- A user can exit the system with no defined return path
- Children's content links to any adult conversion page

All broken flow conditions must be treated as system errors, not edge cases.

### What must never be displaced by a side path

The following elements of the primary funnel must not be overridden, replaced, or bypassed by any topic branch:
- The index page's primary call to action
- The offer page's structure and single-focus design
- The protocol sequence for post-purchase onboarding
- The continuation page's role as the long-term engagement hub

---

## 6. STRUCTURED OUTPUT TABLE

| Topic | Entry Page | Free Step | Trust Step | Offer | Post-Offer (Accept) | Post-Offer (Decline) | Forbidden Transitions |
|---|---|---|---|---|---|---|---|
| Awakening / Matrix / Inner Authority | `/awakening` | Free article or video on conditioning | `/vaatlus/awakening` | `/offer/awakening` | `/success` → `/protocol` → `/continuation/awakening` | Soft deep-dive article. No re-offer same session. | → children content, → courses catalog, → services, → cross-topic during active path |
| Meditations / Affirmations | `/meditations` | Free audio (1 item, no gate) | `/vaatlus/meditations` | `/offer/meditations` | `/success` → `/protocol` → `/continuation/meditations` | Return to free audio library. No re-offer prompt. | → awakening funnel, → children content, → courses during active path |
| Children Content (Angel Tales) | `/angel-tales` | Free story or episode, no registration | `/angel-tales/about` | `/angel-tales/collection` | Download/access confirmation. No protocol. | Return to free episode page. No prompts. | → any adult content, → main funnel CTAs, → urgency framing, → email capture before free access |
| Courses / Learning Programs | `/courses` | Free module or intro lesson, no gate | `/vaatlus/courses` | `/offer/courses/[slug]` | Course onboarding. Access confirmation. | Return to course catalog. No pop-ups. | → services booking during active path, → upsell on offer page, → price before description |
| Services / Sessions | `/services` | Session description and expectations | `/vaatlus/services` | `/offer/services/[slug]` | Booking confirmation. Session prep instructions. No upsell. | Return to services overview. No follow-up automation. | → dependency framing, → discounts/urgency on booking, → accessible from children's content |

---

## APPENDIX: FAILURE CONDITIONS REFERENCE

The navigation system has failed if any of the following are true:

1. A user can access an offer page without completing the trust-building step
2. Children's content displays a link to any adult conversion page
3. A page exists with no defined outbound path
4. More than two choices are presented at any single stage
5. The same offer appears twice in one session after a decline
6. Cross-topic links appear during entry, free value, or trust-building stages
7. The primary funnel is bypassed by any topic branch
8. A user in the Angel Tales path encounters urgency language, countdown timers, or scarcity tactics
9. Any path terminates without a defined soft exit

---

## APPENDIX: AGENT USAGE INSTRUCTIONS

Agents consuming this file must:

1. Identify the user's topic on entry
2. Assign them to the corresponding topic branch
3. Check current stage against the stage sequence
4. Return only the next defined step — never multiple options
5. Enforce forbidden path rules before generating any link or redirect
6. Flag any request that would create a cross-audience connection not permitted by Section 4
7. Treat any undefined path state as a routing error and return the user to the topic entry page
