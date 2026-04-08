# VISUAL DIRECTION v1.0

**Task ID:** WEB-001
**Brand:** Aurin Beyond / Aurin OS
**Layer:** Visual Identity / Design System
**Status:** Active

---

## CORE PRINCIPLE

> Depth. Clarity. Calm power.

The visual system does not decorate. It communicates.

---

## BRAND DESIGN DNA

| Element | Value |
|---------|-------|
| Background | `#050505` — near-black |
| Primary text | `rgba(255, 255, 255, 0.9)` — soft white |
| Accent | `#d4af37` — gold |
| Font | `Inter`, sans-serif |
| Layout | Ultraminimalist, centered, high contrast |
| Motion | Subtle fade-ins, no flash |
| Density | Low. White space is intentional. |

---

## VISUAL FEELING

The site must feel like:

- Entering a space where clarity is possible
- A system — not a product catalogue
- Intelligence, not decoration
- Authority earned through restraint, not volume

**References (feeling, not style):**
- A dark room where one object is lit
- A long pause before a precise sentence
- Architecture that says nothing unnecessary

---

## STYLE RULES

### 1. BACKGROUNDS

- Base: `#050505` (near-black)
- Depth layers: `rgba(255, 255, 255, 0.02–0.05)` glass panels
- Gradient: subtle radial glow — from `#111` center, fading to `#050505`
- No full-color backgrounds
- No gradients that compete with content

---

### 2. TYPOGRAPHY

| Use | Style |
|-----|-------|
| Page headline (H1) | `Inter` 600, large, white |
| Section headline (H2) | `Inter` 400, medium, white |
| Body / explanation | `Inter` 300, regular, `rgba(255,255,255,0.8)` |
| Labels / eyebrow | `Inter` 300, uppercase, letter-spacing: 2px, gold or muted |
| CTA button | `Inter` 600, gold text or gold border on dark |

**Rules:**
- No decorative fonts
- No more than 2 type sizes per section
- Line length: max 600–700px for readability
- Line height: 1.6–1.8 for body text

---

### 3. GLASS PANELS (Card UI)

Used for: product panels, feature cards, protocol blocks

```css
background: rgba(255, 255, 255, 0.03);
border: 1px solid rgba(212, 175, 55, 0.3);
border-radius: 16px;
backdrop-filter: blur(10px);
```

- Gold border at low opacity — present but not loud
- Background barely lifted from page base
- No drop shadows (they add weight; this system uses light, not shadow)

---

### 4. CTA BUTTONS

```css
/* Primary CTA */
background: transparent;
border: 1px solid #d4af37;
color: #d4af37;
padding: 14px 32px;
border-radius: 4px;
font-weight: 600;
letter-spacing: 1px;

/* Hover state */
background: rgba(212, 175, 55, 0.1);
```

- Gold outline on dark background
- No filled buttons except for maximum-priority actions
- One primary CTA per page

---

### 5. NAVIGATION

```css
/* Nav links */
color: rgba(255, 255, 255, 0.7);
font-size: 0.9rem;
letter-spacing: 1px;

/* Active page */
color: #d4af37;
```

- Minimal, horizontal
- No hamburger menus unless mobile-forced
- Brand name / logo: left-aligned on desktop

---

### 6. IMAGES AND VISUALS

**Style:** Cinematic, symbolic, non-generic.

**IMAGE APPROVAL FILTER**

Before any image is used on any surface, apply this test in order:

| Test | Result |
|------|--------|
| Does it directly communicate the idea? | If NO → **DO NOT USE IT** |
| Is it decorative only (no conceptual function)? | If YES → **REJECT** |
| Does it create emotional + conceptual clarity simultaneously? | If YES → **APPROVE** |

One test. No exceptions. An image that passes rule 3 automatically passes rules 1 and 2.

**Rules:**
- No stock photography
- No lifestyle images (people smiling at laptops)
- No cartoon/illustration style
- Images must be atmosphere **and** meaning — not atmosphere alone
- Images support the text — they do not replace it
- Max 1 main visual per page section

**Approved visual concepts:**
- Light emerging from darkness (void/transition)
- Geometric abstraction (structure/system)
- Human silhouette with depth (observation/awareness)
- Empty space with one point of light (clarity/focus)
- Grid or system lines, subtle (architecture)
- Abstract fluid forms in near-black (consciousness/pattern)

---

### 7. SPACING AND LAYOUT

| Zone | Rule |
|------|------|
| Section padding | Minimum 80px vertical |
| Max content width | 900px centered |
| Card grid | 3-column on desktop, 1-column on mobile |
| Hero section | Full viewport height or minimum 60vh |
| Between sections | 60–80px gap |

**Space is not empty. Space is deliberate.**

---

### 8. MOTION AND TRANSITIONS

- Fade-in on page load: `opacity 0 → 1`, duration `0.6–0.8s`
- No slide animations (movement = distraction)
- No scroll-triggered animations unless extremely subtle
- No looping background animations
- Button hover: color transition `0.2s ease`

---

## PAGE-SPECIFIC VISUAL DIRECTION

| Page | Visual Atmosphere |
|------|-----------------|
| `index.html` | Dark base. Soft radial glow in center. Headline centered. Single CTA below. Stillness. |
| `vsl.html` | System-feel. Three cards in grid. Subtle structure. VSL placeholder dark with one light point. |
| `offer.html` | Premium. Gold accent panel centered. High contrast between dark bg and gold border. |
| `success.html` | Lighter feel — confirmation, not sales. Neutral dark with soft affirmative tone. |
| `protocol.html` | Operational. Clean structure. Steps clear. No visual noise. |
| `disclaimer.html` | Clean, neutral. Light text on dark. No decorative elements. |
| `void.html` | Entry into depth. Atmospheric. Longest pause before structure. |
| ARKANA pages | Abstract, geometric, progressive depth as user moves through chain. |

---

## WHAT DOES NOT BELONG

| Forbidden | Reason |
|-----------|--------|
| Bright color backgrounds | Contradiction with brand depth |
| Multiple competing CTAs | Dilutes action |
| Decorative icon packs | Adds noise |
| Centered justified text | Reduces readability |
| Large hero images with text overlay | Creates illegibility |
| Animated hero backgrounds | Distracts from message |
| Stock photo humans | Breaks cinematic abstraction |

---

## MOBILE RULES

- Font scale: H1 max `2.2rem` on mobile
- Padding: minimum `24px` horizontal
- Cards: single column, full width
- CTA: full width button on mobile
- Navigation: simplified horizontal or stacked

---

## CSS CANONICAL FILE

All styles must be in one of:
- `style.css` (root — currently active)
- `assets/css/style.css` (per SYSTEM_RULES.md architecture — resolve after audit)

**Until CSS architecture is resolved (ISSUE-008):** use `style.css` at root.

---

STATUS: Active // Pure Soul Life / Aurin Beyond // GENESIS Visual Layer
