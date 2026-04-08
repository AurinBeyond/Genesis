# VISUAL IMPLEMENTATION v1.0

**Task ID:** VISUAL-002  
**Brand:** Aurin Beyond / Pure Soul Life  
**Layer:** Visual Identity — Global Implementation  
**Scope:** Website · Gumroad · Social · Product Previews  
**Status:** Active

---

## CORE LAW

> Visual stops the user.  
> Text moves the user.

No surface goes live without a visual anchor.  
One anchor per location. Not more. Never zero.

---

## DESIGN TOKENS (canonical)

These values govern every surface. Do not deviate.

| Token | Value | Usage |
|-------|-------|-------|
| Background base | `#05070a` | All backgrounds |
| Background soft | `#0b0f14` | Cards, elevated surfaces |
| Background deep | `#030508` | Deepest layers, footers |
| Gold accent | `#c5a059` | CTAs, highlights, borders |
| Text primary | `#e6edf3` | All body text |
| Text muted | `#8b949e` | Secondary text, nav links |
| Border | `rgba(197, 160, 89, 0.12)` | Cards, panels |
| Border active | `rgba(197, 160, 89, 0.30)` | Hover states |
| Font | `Inter`, -apple-system, sans-serif | All text |

> **Note:** The canonical gold value in `style.css` is `#c5a059`. Earlier docs referenced `#d4af37`. Use `#c5a059` on all new surfaces.

---

## IMAGE RULES (all channels)

| Rule | Enforcement |
|------|-------------|
| No stock photography | Hard block |
| No human faces | Silhouettes only if human form is needed |
| No text baked into images | Text is always separate overlay |
| No bright or saturated colors | Black, soft white, faint gold only |
| No AI-obvious plastic aesthetics | Photorealistic atmosphere required |
| Every image must work on dark bg | Test against `#05070a` before use |
| File format | PNG or WebP |
| Max file size (web) | 300 KB after compression |

---

## CHANNEL 1 — WEBSITE PAGES

See `IMAGE-PROMPTS.md` for per-page generation prompts.  
See `VISUAL-MAP.md` for per-page layout specs.

### Anchor requirement per page

| Page | Visual Anchor | Type |
|------|--------------|------|
| `index.html` | Single gold light from void | Background/hero image |
| `vsl.html` | Geometric concentric rings | Section header image |
| `offer.html` | Depth-layer architecture | Panel background |
| `success.html` | Door ajar, line of light | Hero image |
| `protocol.html` | Lit desk, single page | Subtle header |
| `gateway.html` | Language selector — radial glow | Background treatment |
| `void.html` | Atmospheric void/mist | Full-page background |
| `core.heart.html` | Hub convergence geometry | Header |
| `delta.insight.html` | Neural geometry, gold lines | Header |
| `sigma.core.html` | Compressed energy core | Header |
| `sigma-protocol.html` | Vertical gold beam | Full-page element |
| `index-en.html` | Same as `index.html` | Background/hero image |
| Legal pages | Two intersecting clean lines | Minimal header |

### Placement standard

```
Hero section:  image sits behind or above headline — never overlapping text
Section break: max 1 image per section
Card visual:   icon or abstract mark inside glass-card, not photo
```

---

## CHANNEL 2 — GUMROAD

### Listing Cover Image

**Dimensions:** 960 × 1280 px (4:5 ratio — Gumroad recommended)  
**Format:** PNG or WebP  
**Placement:** Primary product listing image — first thing buyer sees

**Generation prompt:**

```
Minimalist digital product cover, 4:5 portrait orientation.
Background: near-black #05070a.
A single point of soft gold light (#c5a059) at upper center, diffusing gently outward in concentric halos.
Bottom third: product title area — leave clean, no generated text.
No objects. No figures. No gradients competing with darkness.
Fine film grain texture. Depth of field suggestion.
Editorial photography quality. Ultra-premium feel.
```

**Text overlay (apply in Canva / Figma, not in generation):**

```
Line 1: THE SOURCE WITHIN  — Inter 600, white, 48px, centered
Line 2: Entry System        — Inter 300, gold #c5a059, 24px, centered, letter-spacing 4px
```

---

### Product Thumbnail (library view)

**Dimensions:** 600 × 600 px (1:1)  
**Used in:** Gumroad creator library, link previews

**Generation prompt:**

```
Square format product thumbnail.
Background: absolute black.
Center: single circular halo of soft gold light — no object at source, only diffused glow.
Completely minimal. Cinematic. No text generated.
Film grain. 1:1 aspect ratio. Ultra-high contrast.
```

**Text overlay:**

```
Line 1: THE SOURCE WITHIN — Inter 600, white, 32px
Line 2: aurinbeyond.gumroad.com — Inter 300, muted, 14px
```

---

### Checkout Page (Gumroad — cannot fully style, but control what you can)

- Set cover image (above)
- Ensure product name reads correctly in Gumroad's own UI
- No custom HTML in checkout — visual is carried by the cover alone

---

## CHANNEL 3 — SOCIAL POSTS

### Format standards

| Platform | Ratio | Dimensions |
|----------|-------|-----------|
| Instagram Post | 1:1 | 1080 × 1080 px |
| Instagram Story / Reel cover | 9:16 | 1080 × 1920 px |
| Twitter/X post image | 16:9 | 1200 × 675 px |
| LinkedIn post image | 1.91:1 | 1200 × 627 px |

---

### Visual types

**Type A — Statement post (text-first)**

```
Background: #05070a solid or with very subtle radial glow.
Text: 1–3 lines maximum. Inter 600, white. Large.
Accent: one word or line in gold #c5a059.
No image. The emptiness IS the visual.
Bottom: aurinbeyond logo or URL — small, muted.
```

**Generation prompt (background texture only):**

```
Ultra-dark background texture, near-black #05070a,
imperceptible fine grain, absolutely no objects or light sources,
pure atmospheric base for text overlay,
aspect ratio [choose per platform], 4K seamless
```

---

**Type B — Atmospheric post (image-first)**

```
Full-bleed cinematic image with minimal text overlay at bottom.
Image generates the stop. Text delivers the idea.
Max 6 words of text on the image.
Full caption text lives in the post body, not the image.
```

**Generation prompt:**

```
Cinematic atmospheric photograph.
Deep black background #05070a.
Single dramatic element: [choose from approved concepts below].
Soft gold or white light only. No color cast.
Film grain, editorial quality.
No people, no faces, no text.
[platform ratio]
```

**Approved visual concepts for social:**

| Concept | Feeling | Use for |
|---------|---------|---------|
| Single gold light from void | Emergence, source | Product launch, key statements |
| Geometric lines converging | Structure, system | Protocol / system posts |
| Empty dark room, one open door | Threshold, permission | Entry posts, invitations |
| Vertical gold beam in darkness | Precision, will | Action-call posts |
| Abstract neural geometry | Recognition, pattern | Insight posts |
| Atmospheric mist, deep void | Before awareness | Depth / philosophy posts |

---

**Type C — Product preview post**

```
Repurpose Gumroad cover (960×1280) cropped to platform ratio.
Add context in caption, not in image.
CTA in caption: link in bio or direct URL.
```

---

### Social visual rule

Every post has one of:
1. A visual anchor image (Types B or C), OR
2. A typographic composition with intentional negative space (Type A)

A plain text post with no visual logic is not published.

---

## CHANNEL 4 — PRODUCT PREVIEWS

Product previews are the images shown inside the Gumroad listing — they demonstrate what the buyer receives before purchasing.

### Preview image 1 — Cover page of PDF

**Dimensions:** 1600 × 900 px (16:9)  
**Shows:** The opening page of `source-within.pdf` — title, no content visible

**Design spec:**

```
Background: #05070a
Top center: THE SOURCE WITHIN — Inter 600, white, 64px
Below: Entry System — Inter 300, gold #c5a059, 28px, letter-spacing 6px
Below: A Guide to Internal Authority — Inter 300, muted, 18px
Bottom: Pure Soul Life — Inter 300, gold, 14px, very low opacity
Vertical rhythm: generous spacing, nothing crowded
```

---

### Preview image 2 — Interior page sample

**Dimensions:** 1600 × 900 px (16:9)  
**Shows:** One section heading + 3–4 lines of body text — proof of format and density

**Design spec:**

```
Background: white or very light warm grey (#f5f5f0) — PDF interior is light
Section heading: Inter 600, dark, 28px
Body text: Inter 300, dark, 16px, line-height 1.8
Margin: generous — shows the document breathes
No clutter. Demonstrates: this is not a wall of text.
```

---

### Preview image 3 — System connection visual

**Dimensions:** 1600 × 900 px (16:9)  
**Shows:** Where this product fits in the larger system (visual diagram)

**Design spec:**

```
Background: #05070a
Center: entry node labeled "Source Within" — gold circle
Arrow right: next node "Protocol" — muted circle
Text: "This is Layer 1." — Inter 300, muted, centered below
Communicates: this is part of a system, not a standalone purchase.
```

---

## IMPLEMENTATION CHECKLIST

### Before any page or product goes live:

- [ ] Visual anchor identified for this surface
- [ ] Image generated or sourced (from approved concepts)
- [ ] Image tested on dark background (`#05070a`)
- [ ] File compressed under 300 KB
- [ ] Text overlay applied separately (not baked into generation)
- [ ] Alt text written (descriptive)
- [ ] No stock aesthetics present

### Gumroad-specific:

- [ ] Cover image (960×1280) uploaded
- [ ] Thumbnail (600×600) ready for library
- [ ] Preview images 1–3 uploaded in order

### Social-specific:

- [ ] Post type selected (A / B / C)
- [ ] Visual concept assigned from approved list
- [ ] Caption carries the full message — image carries the stop

---

## FORBIDDEN (all channels)

| Element | Reason |
|---------|--------|
| Stock photography | Breaks cinematic abstraction |
| Human faces | Brand uses no identifiable people |
| Bright / saturated color | Contradicts depth principle |
| Text baked into generated images | Impossible to maintain consistency |
| Multiple accent colors | Gold only |
| Decorative graphic elements (arrows, stars, stickers) | Visual noise |
| Platform-default cover placeholders | No visual anchor = not live |
| Animated backgrounds on web | Distraction from text |

---

## REFERENCE DOCUMENTS

| Document | Purpose |
|----------|---------|
| `VISUAL-DIRECTION.md` | Brand DNA, style rules, CSS variables |
| `IMAGE-PROMPTS.md` | Generation prompts per website page |
| `VISUAL-MAP.md` | Per-page layout and visual specs |
| `style.css` | Canonical CSS — source of truth for all token values |
| `GUMROAD-PACK.md` | Product setup — includes cover image prompt |

---

STATUS: Active // Aurin Beyond / Pure Soul Life // GENESIS Visual Implementation Layer
