# ARKANA-OS // SYSTEM RULES v1.2

Käesolev dokument on kohustuslik juhis igale tehisintellektile (AI), kes tegeleb ARKANA-OS arenduse, parandamise või viimistlemisega.

---

## 1. SÜSTEEMI EESMÄRK
ARKANA-OS on minimalistlik kognitiivse juhtimise süsteem, mille eesmärk on:
- Vähendada digitaalset ja sisemist müra.
- Katkestada automaatne reaktsioon ja suunata tähelepanu teadlikumaks.
- Säilitada lineaarne, rahulik ja häirimatu kasutajavoog.

---

## 2. DISAINIKEEL (VISUAL IDENTITY)
- **Taust:** `#050505` (sügav must)
- **Põhitekst:** `rgba(255, 255, 255, 0.9)`
- **Aktsent:** `#d4af37` (kuldne)
- **Font:** 'Inter', sans-serif (Google Fonts)
- **Stiil:** Ultraminimalistlik, monokroomne, kõrge kontrastsusega.
- **Mobiil:** Mobile-first; alati kontrollida visuaalset stabiilsust alla 600px laiusel.

---

## 3. ARHITEKTUURI REEGLID
- **Failinimed:** kebab-case (nt `sigma-protocol.html`).
- **Süsteemi voog (kohustuslik):**
  `index -> void -> core -> delta-insight -> sigma-core -> sigma-protocol`.
- **CSS:** Kõik ühised stiilid peavad asuma failis `assets/css/style.css`.
- **Kood:** Kasutada ainult Vanilla HTML, CSS ja JavaScripti. Välised raamistikud on keelatud.

---

## 4. LUBATUD TEGEVUSED (AI AGENDILE)
- CSS-i optimeerimine ja koondamine ühte keskseks failiks.
- Mobiilivaate parandamine (responsive design, padding, spacing).
- Semantilise HTML-i tugevdamine (main, section, nav, aria-labels).
- Spacingu, loetavuse ja interaktsioonide (focus-states) ühtlustamine.

---

## 5. KEELATUD TEGEVUSED
- **Ära muuda** sisu filosoofilist tähendust ega põhitekste ilma loata.
- **Ära muuda** failistruktuuri ega lineaarset voogu.
- **Ära kasuta** väliseid raamistikke (React, Tailwind, Bootstrap jne).
- **Ära muuda** brändi värve, fonti ega nime omal algatusel.

---

## 6. KRITIILISED KAITSED
- **LocalStorage:** Ära muuda ega lõhu LocalStorage loogikat failis `delta-insight.html`.
- **User Input:** Ära eemalda ega muuda kasutaja sisestatud andmete säilitamise loogikat.
- **Review:** AI väljund ei ole automaatselt lõplik. Kõik muudatused vajavad süsteemi omaniku kinnitust.

---

## 7. PRIORITEETIDE JÄRJEKORD
Konflikti korral järgi seda pingerida:
1. Süsteemi filosoofia ja eesmärk.
2. Lineaarne kasutajavoog.
3. Mobiilistabiilsus ja loetavus.
4. Visuaalne viimistlus ja tehniline puhtus.

---
STATUS: Locked as Baseline // 2026 // Operational Clarity
