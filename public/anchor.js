(function () {
    // 1. LOOME FOOTERI STRUKTUURI
    const footer = document.createElement('footer');
    footer.style.cssText = "margin-top: 100px; padding: 60px 20px; text-align: center; opacity: 0.3; font-family: 'Inter', sans-serif;";
    footer.innerHTML = `
        <div style="font-size: 0.65rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 15px; color: white;">
            &copy; 2026 Aurin OS // Genesis
        </div>
        <div style="font-size: 0.75rem;">
            <a href="termsA.html" style="color: white; text-decoration: none; margin: 0 10px;">Vastutus</a>
            <span style="color: rgba(255,255,255,0.2);">|</span>
            <a href="termsB.html" style="color: white; text-decoration: none; margin: 0 10px;">Privaatsus</a>
            <span style="color: rgba(255,255,255,0.2);">|</span>
            <a href="#" id="open-cookies" style="color: white; text-decoration: none; margin: 0 10px;">Küpsised</a>
            <span style="color: rgba(255,255,255,0.2);">|</span>
            <a href="mailto:contact.puresoul@proton.me" style="color: white; text-decoration: none; margin: 0 10px;">Tugi</a>
        </div>
    `;

    // 2. LOOME BÄNNERI STRUKTUURI
    const banner = document.createElement('div');
    banner.id = 'cookie-banner';
    banner.style.cssText = "display:none; position:fixed; bottom:0; left:0; width:100%; background:rgba(5,5,5,0.98); border-top:1px solid rgba(212,175,55,0.3); backdrop-filter:blur(15px); z-index:10000; padding:20px; font-family:'Inter', sans-serif;";
    banner.innerHTML = `
        <div style="max-width:1000px; margin:0 auto; display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:20px;">
            <p style="color:rgba(255,255,255,0.8); font-size:0.8rem; line-height:1.6; margin:0; font-weight:300; flex:1 1 500px;">
                Aurin OS kasutab anonüümset analüütikat süsteemi optimeerimiseks. Analüütika aktiveeritakse ainult sinu nõusolekul. 
                <a href="termsB.html" style="color:#d4af37; text-decoration:none; border-bottom:1px solid rgba(212,175,55,0.2);">Vaata põhimõtteid</a>.
            </p>
            <div style="display:flex; gap:10px; flex-wrap:wrap;">
                <button id="decline-cookies" style="background:transparent; border:1px solid rgba(255,255,255,0.25); color:rgba(255,255,255,0.8); padding:10px 20px; font-size:0.7rem; text-transform:uppercase; letter-spacing:2px; cursor:pointer;">Keeldun</button>
                <button id="accept-cookies" style="background:transparent; border:1px solid #d4af37; color:#d4af37; padding:10px 25px; font-size:0.7rem; text-transform:uppercase; letter-spacing:2px; cursor:pointer;">Nõustun</button>
            </div>
        </div>
    `;

    // 3. LISAME ELEMENDID LEHELE
    document.body.appendChild(footer);
    document.body.appendChild(banner);

    // 4. LOOGIKA
    const STORAGE_KEY = 'aurin_cookie_consent';

    const show = () => banner.style.display = 'block';
    const hide = () => banner.style.display = 'none';

    document.getElementById('accept-cookies').onclick = () => {
        localStorage.setItem(STORAGE_KEY, 'accepted');
        hide();
        console.log('Aurin OS: Consent accepted');
    };

    document.getElementById('decline-cookies').onclick = () => {
        localStorage.setItem(STORAGE_KEY, 'declined');
        hide();
        console.log('Aurin OS: Consent declined');
    };

    document.getElementById('open-cookies').onclick = (e) => {
        e.preventDefault();
        localStorage.removeItem(STORAGE_KEY);
        show();
    };

    if (!localStorage.getItem(STORAGE_KEY)) show();
})();
<script src="anchor.js"></script>
