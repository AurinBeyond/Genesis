# VISUAL MAP v1.0

**Task ID:** WEB-002
**Brand:** Aurin Beyond / Aurin OS
**Layer:** Visual / Design Consistency
**Status:** Active

---

## PURPOSE

Define visual consistency across all pages.
Every page must be recognizably part of the same system.

---

## GLOBAL STYLE

| Variable | Value |
|----------|-------|
| Background base | `#050505` |
| Text primary | `rgba(255, 255, 255, 0.9)` |
| Text secondary | `rgba(255, 255, 255, 0.6)` |
| Accent gold | `#d4af37` |
| Glass panel | `rgba(255, 255, 255, 0.03)` |
| Gold border (low) | `rgba(212, 175, 55, 0.3)` |
| Font | `Inter`, sans-serif (Google Fonts) |
| Border radius | `16px` (cards), `4px` (buttons) |
| Blur (glass) | `backdrop-filter: blur(10px)` |

---

## IMAGE STYLE

| Attribute | Rule |
|-----------|------|
| Tone | Cinematic, symbolic |
| Color palette | Black, soft white, faint gold |
| Human content | Silhouettes only, no faces |
| Text in images | Never |
| Stock aesthetics | Forbidden |
| Resolution | Minimum 1920×1080 |
| Format | PNG or WebP |

---

## PAGE VISUAL RULES

---

### HOME (`index.html`)

| Element | Specification |
|---------|--------------|
| Background | `#050505` with very subtle radial glow at center |
| Hero | Fullscreen or 80vh, centered content |
| Visual | Soft golden light from darkness — see `IMAGE-PROMPTS.md` |
| Primary CTA | Gold outline button, centered below headline |
| Motion | Fade-in on load only |
| Density | Lowest — maximum white space |

---

### OBSERVATION (`vsl.html`)

| Element | Specification |
|---------|--------------|
| Background | `#050505`, fine grid overlay at 3% opacity |
| Content | Centered hero + 3-card glass grid below |
| Visual | Abstract system lines converging |
| Cards | `glass-card` class — gold border at `rgba(212,175,55,0.3)` |
| CTA | Gold outline, below card grid |

---

### ACADEMY / OFFER (`offer.html`)

| Element | Specification |
|---------|--------------|
| Background | `#050505`, no overlay |
| Product panel | Centered glass panel, max-width 600px |
| Panel border | `1px solid rgba(212, 175, 55, 0.3)` |
| Visual | Premium depth layers image — see `IMAGE-PROMPTS.md` |
| Price | Gold accent color |
| CTA | Gold outline, centered in panel |
| Footer links | Small text, low opacity, bottom of page |
| Density | Medium — enough space to breathe, enough content to decide |

---

### CONFIRMATION (`success.html`)

| Element | Specification |
|---------|--------------|
| Background | `#050505` — marginally warmer feeling |
| Tone | Confirmatory, not transactional |
| Visual | Door ajar with light — see `IMAGE-PROMPTS.md` |
| Navigation cards | Max 3, glass style, horizontal or stacked |
| Support email | Visible, not buried |
| CTA | Protocol button — gold outline |

---

### PROTOCOL (`protocol.html`)

| Element | Specification |
|---------|--------------|
| Background | Flat `#050505`, no visual distractions |
| Layout | Linear, step-by-step — numbered or sequential |
| Typography | Clear hierarchy — step number in gold, content in white |
| Visual | Single desk in light — used as subtle header |
| CTA | None external — protocol is the action |
| Density | Medium — content is the product |

---

### LEGAL PAGES (`disclaimer.html`, `client-agreement.html`, `pricing-policy.html`, `terms.html`)

| Element | Specification |
|---------|--------------|
| Background | `#050505`, no image |
| Typography | Clean hierarchy — heading + body text |
| Decoration | None |
| Back link | Top of page, low-opacity arrow link |
| Visual | None or minimal geometric placeholder |
| Width | Max 800px, readable columns |

---

### VOID PAGE (`void.html`)

| Element | Specification |
|---------|--------------|
| Background | Absolute black with atmospheric mist — deepest density |
| Visual | Atmospheric void image — see `IMAGE-PROMPTS.md` |
| Navigation | Minimal — one forward link |
| Typography | Sparse — fewer words than any other page |
| Feeling | Entry into depth — stillness before structure |

---

### ARKANA-OS CHAIN (core → delta → sigma-core → sigma-protocol)

| Page | Visual Progression |
|------|--------------------|
| `core.html` | Hub convergence — lines meeting at center — structure established |
| `delta.insight.html` | Neural geometry — complexity mapped — pattern visible |
| `sigma.core.html` | Compression — density increases — essence distilled |
| `sigma-protocol.html` | Single beam — pure execution — maximum precision |

The visual intensity increases as the user moves through the chain.
Each page is slightly more focused, slightly more compressed.

---

## NAVIGATION VISUAL STANDARD

| State | Style |
|-------|-------|
| Default link | `rgba(255, 255, 255, 0.7)` |
| Active page | `#d4af37` (gold) |
| Hover | `rgba(255, 255, 255, 1.0)` |
| Logo / Brand name | White, font-weight 600 |

---

## CTA BUTTON STANDARD

| State | Style |
|-------|-------|
| Default | `border: 1px solid #d4af37; color: #d4af37; background: transparent` |
| Hover | `background: rgba(212, 175, 55, 0.1)` |
| Active/Pressed | `background: rgba(212, 175, 55, 0.2)` |
| Size | `padding: 14px 32px`, `border-radius: 4px` |

One primary CTA per page. Never two gold buttons competing.

---

## FOOTER STANDARD

All pages share the same footer:

```
© 2026 Aurin OS | [Liability disclaimer link]
```

- Small text, low opacity
- Gold link on hover
- No extra content

---

## SYSTEM CONNECTION MAP

| Page | Traffic Source | Next Destination |
|------|---------------|-----------------|
| `index.html` | Social / direct link | `vsl.html` |
| `vsl.html` | `index.html` | `offer.html` |
| `offer.html` | `vsl.html` | Gumroad |
| `success.html` | Gumroad redirect | `protocol.html` |
| `protocol.html` | `success.html` | Continuation |
| Legal pages | `offer.html` footer | Back to `offer.html` |

---

## FORBIDDEN (visual)

| Element | Why |
|---------|-----|
| Bright color backgrounds | Breaks brand depth |
| Multiple accent colors | Gold only |
| Drop shadows on cards | Use light, not shadow |
| Serif or display fonts | Inter only |
| Decorative dividers (horizontal rules styled) | Increases noise |
| Fullscreen image backgrounds with text overlay | Creates illegibility |
| Animations beyond fade-in | Distraction |
| Multiple CTAs on one page | Removes clarity of action |

---

## VALIDATION

| Check | Status |
|-------|--------|
| Background consistent across all pages | ✅ `#050505` base |
| Accent color used consistently | ✅ `#d4af37` only |
| CTA style identical across all pages | ✅ Gold outline |
| Font consistent | ✅ `Inter` everywhere |
| No page has visual identity mismatch | ✅ |
| All pages recognizable as same system | ✅ |

---

STATUS: Active // Pure Soul Life / Aurin Beyond // GENESIS Visual Consistency Layer
