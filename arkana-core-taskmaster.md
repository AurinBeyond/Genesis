# ARKANA-OS // TASKMASTER v1.2

See on süsteemi operatiivne aju ja juhtimiskeskus. Kõik arendustööd, parandused ja viimistlused peavad lähtuma käesolevast failist ning alluma rangelt `SYSTEM_RULES.md` eeskirjadele.

---

## 🧠 TÖÖREEGEL (OPERATIONAL PROTOCOL)

- **Fookus:** AI (Agent) töötab eranditult ainult **ACTIVE** sektsioonis määratud ülesannetega.
- **Järjekord:** Ülesandeid täidetakse ühekaupa (Serial Processing), et tagada süsteemi stabiilsus.
- **Infrastruktuur:** Iga koodimuudatus peab läbima `.github/workflows/deploy.yml` kontrolli.
- **Piirang:** AI ei tohi alustada NEXT või BACKLOG ülesandeid ilma omaniku otsese loata.

---

## 🔴 ACTIVE (Päev 1: Arhitektuuri lukustamine)

AI peab teostama järgmised sammud ranges järjekorras:

1. **Global Stylesheet Integration**
   - Loo kataloog: `assets/css/`
   - Loo fail: `assets/css/style.css`
   - Koonda sinna kõigi 6 HTML-faili ühine visuaalne kood (DNA), eemaldades duplikaadid.

2. **HTML Sanitization**
   - Eemalda kõik `<style>` blokid HTML failidest.
   - Lisa igasse `<head>` sektsiooni viide: `<link rel="stylesheet" href="assets/css/style.css">`.

3. **Internal Link Audit**
   - Kontrolli ja taga katkematu ahel (Zero Broken Links):
     `index -> void -> core -> delta-insight -> sigma-core -> sigma-protocol`.

4. **Validation Run**
   - Veendu, et süsteem läbib CI/CD kontrolli (Strict file audit & Stylesheet link validation).

---

## 🟡 NEXT (Mobiil & UX viimistlus)

- [ ] **Mobile-First Spacing:** Optimeerida vaade vahemikus 320px - 600px.
- [ ] **Accessibility:** Implementeerida `:focus-visible` ja kontrollida `aria-label` staatust.
- [ ] **Typography:** Optimeerida 'Inter' fondi laadimine ja headingute vahed.

---

## 🔵 BACKLOG (Tulevikuideed)

- [ ] **Page Transitions:** Minimalistlikud fade-in üleminekud lehtede vahel.
- [ ] **Data Management:** LocalStorage andmete eksportimise võimalus (JSON/CSV).
- [ ] **Identity:** ARKANA-OS unikaalse monokroomse faviconi loomine.

---

## ✅ VALMIS TÖÖ DEFINITSIOON (DoD)

Ülesanne loetakse lõpetatuks ("Done") vaid siis, kui:
1. GitHub Actions töövoog on **ROHELINE** (`Success`).
2. `assets/css/style.css` on füüsiliselt olemas ja kõik 6 lehte viitavad sellele.
3. Visuaalne keel (Must #050505 / Kuldne #d4af37) on säilinud muutumatuna.
4. Süsteemi lineaarne voog on testitud ja toimib tõrgeteta.

---

## 🔁 TÖÖTSÜKKEL

1. **Input:** Omanik uuendab või kinnitab ACTIVE sektsiooni.
2. **Execute:** AI genereerib vajaliku koodi või parandused.
3. **Push:** Omanik teostab `git push origin main`.
4. **Verify:** GitHub Actions kinnitab töö korrektsuse ja teostab automaatse deploy.

---

STATUS: Operational // Version 1.2 // 2026 // ARKANA-OS Deployment Ready
