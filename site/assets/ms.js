/* ============================================================
   MOONSHIFT STUDIO — APP LINKS
   This is the ONLY place to edit when an app launches.
   Paste the App Store / Google Play links below. Every QR code
   already printed keeps working, because QR codes point to
   moonshiftstudio.com/get/<app> and that page sends people to
   the right store for their phone.
   ============================================================ */
window.MOONSHIFT_APPS = {
  nopehook: {
    name: 'Nopehook', page: 'apps/nopehook.html',
    ios: '',        // App Store link, e.g. https://apps.apple.com/app/id0000000000
    android: '',    // Google Play link, e.g. https://play.google.com/store/apps/details?id=com.moonshiftstudio.nopehook
    web: '',        // Web app link, once public
    soon: 'Nopehook is in development. Join the testers list to try it early.'
  },
  unbadged: {
    name: 'Unbadged', page: 'apps/unbadged.html',
    ios: '', android: '',
    web: '',        // Leave empty while the beta is invite-only
    soon: 'Unbadged is in an invite-only beta. Email hello@unbadged.app to ask for an invite.'
  },
  'firefly-dash': {
    name: 'Firefly Dash', page: 'apps/firefly-dash.html',
    ios: '', android: '',
    web: 'https://fireflydash.moonshiftstudio.com',
    soon: 'Firefly Dash is free to play in your phone browser right now.'
  },
  'manatable': {
    name: 'Manatable', page: 'apps/manatable.html',
    ios: '', android: '', web: '',
    beta: 'https://manatable.vercel.app/beta.html',   // until a store link is filled in, the QR code opens the beta sign-up
    soon: 'Manatable is in testing. Ask to join the beta to try it early.'
  }
};

/* Tester sign-ups are saved to the Moonshift Supabase table "studio_signups" (insert-only). */
window.MOONSHIFT_SIGNUPS = {
  url: 'https://ynwabowujlalbztriqwj.supabase.co/rest/v1/studio_signups',
  key: 'sb_publishable_PfxVeJHIKIzqtj_X3i9LjQ_rMWts8Dm'
};

(function () {
  var SITE = 'https://moonshiftstudio.com';
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function getUrl(id) { return SITE + '/get/' + id; }
  function platform() {
    var ua = navigator.userAgent || '';
    if (/iPhone|iPad|iPod/i.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1)) return 'ios';
    if (/Android/i.test(ua)) return 'android';
    return 'other';
  }

  /* Header: solid after scrolling, plus the shift clock (10:00 PM at the top, 7:00 AM at the bottom) */
  function header() {
    var head = $('.head'), clock = $('[data-clock]');
    var menuBtn = $('.menu-btn'), nav = $('.nav');
    if (menuBtn && nav) menuBtn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    function tick() {
      var y = window.scrollY || 0;
      if (head && !head.classList.contains('always')) head.classList.toggle('solid', y > 40);
      if (!clock) return;
      var max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      var p = Math.min(1, Math.max(0, y / max));
      var mins = Math.round((22 * 60 + p * 9 * 60) / 5) * 5 % (24 * 60);
      var h = Math.floor(mins / 60), m = mins % 60, ap = h >= 12 ? 'PM' : 'AM';
      var hh = h % 12 || 12;
      clock.textContent = (p > .985 ? 'Clocked out · ' : '') + hh + ':' + (m < 10 ? '0' : '') + m + ' ' + ap;
    }
    window.addEventListener('scroll', tick, { passive: true });
    window.addEventListener('resize', tick);
    tick();
  }

  /* QR codes, drawn as crisp SVG */
  function qrSvg(text) {
    if (typeof window.qrcode !== 'function') return null;
    var qr = window.qrcode(0, 'M'); qr.addData(text); qr.make();
    var n = qr.getModuleCount(), q = 2, size = n + q * 2, d = '';
    for (var r = 0; r < n; r++) for (var c = 0; c < n; c++) if (qr.isDark(r, c)) d += 'M' + (c + q) + ' ' + (r + q) + 'h1v1h-1z';
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + size + ' ' + size + '" shape-rendering="crispEdges" role="img" aria-label="QR code for ' + text + '"><rect width="100%" height="100%" fill="#fff"/><path d="' + d + '" fill="#0B1427"/></svg>';
  }
  function renderQrs() {
    $$('[data-qr]').forEach(function (el) {
      var url = getUrl(el.getAttribute('data-qr'));
      el.innerHTML = qrSvg(url) || '<div class="qr-fallback">' + url + '</div>';
    });
  }
  function saveQr(id, btn) {
    var holder = $('[data-qr="' + id + '"] svg');
    if (!holder) return;
    var img = new Image(), size = 1200;
    img.onload = function () {
      var c = document.createElement('canvas'); c.width = c.height = size;
      var x = c.getContext('2d'); x.imageSmoothingEnabled = false; x.drawImage(img, 0, 0, size, size);
      c.toBlob(function (b) {
        var a = document.createElement('a'); a.href = URL.createObjectURL(b); a.download = 'moonshift-' + id + '-qr.png';
        document.body.appendChild(a); a.click(); a.remove();
        btn.textContent = 'Saved';
      });
    };
    img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(holder.outerHTML);
  }

  function renderStores() {
    $$('[data-stores]').forEach(function (el) {
      var app = window.MOONSHIFT_APPS[el.getAttribute('data-stores')];
      function cell(link, label) {
        return link ? '<a class="store on" href="' + link + '" rel="noopener"><span>Download on</span><b>' + label + '</b></a>'
                    : '<div class="store off"><span>Coming soon to</span><b>' + label + '</b></div>';
      }
      el.innerHTML = cell(app.ios, 'App Store') + cell(app.android, 'Google Play');
    });
  }

  function runLanding() {
    var el = $('[data-landing]');
    if (!el) return;
    var id = el.getAttribute('data-landing'), app = window.MOONSHIFT_APPS[id], p = platform();
    var target = (p === 'ios' && app.ios) || (p === 'android' && app.android) || '';
    if (!target && !app.ios && !app.android && app.web) target = app.web;
    var msg = $('#landing-msg'), btns = $('#landing-btns');
    // creator links: moonshiftstudio.com/c/<code> -> /get/manatable?c=<code>. Count the open (code + time only) and pass the code on.
    var ref = ''; try { ref = (new URLSearchParams(location.search).get('c') || '').toLowerCase(); if (!/^[a-z0-9-]{2,40}$/.test(ref)) ref = ''; } catch (e) {}
    if (ref && id === 'manatable') {
      try { fetch('https://oklqtxcochmwadcdgntd.supabase.co/rest/v1/creator_clicks', {method: 'POST', keepalive: true, headers: {apikey: 'sb_publishable_ybqrInSruSzawTFlYEHq9w_VsXTQDak', Authorization: 'Bearer sb_publishable_ybqrInSruSzawTFlYEHq9w_VsXTQDak', 'Content-Type': 'application/json', Prefer: 'return=minimal'}, body: JSON.stringify({code: ref})}); } catch (e) {}
      var add = function (u, key) { return u ? u + (u.indexOf('?') < 0 ? '?' : '&') + key + '=' + encodeURIComponent(ref) : u; };
      app = Object.assign({}, app, {beta: add(app.beta, 'c'), ios: add(app.ios, 'ct')});   // App Store campaign links use ct=
      target = (p === 'ios' && app.ios) || (p === 'android' && app.android) || target;
    }
    if (!target && !app.ios && !app.android && app.beta) {
      msg.textContent = 'Taking you to the ' + app.name + ' beta sign-up…';
      btns.innerHTML = '<a class="btn btn-gold" href="' + app.beta + '">Join the ' + app.name + ' beta</a><a class="btn btn-ghost" href="../' + app.page + '">About ' + app.name + '</a>';
      setTimeout(function () { location.replace(app.beta); }, 600);
      return;
    }
    if (target) {
      msg.textContent = 'Taking you to ' + app.name + '…';
      btns.innerHTML = '<a class="btn btn-gold" href="' + target + '">Open ' + app.name + '</a>';
      setTimeout(function () { location.replace(target); }, 600);
      return;
    }
    var b = '';
    if (app.ios) b += '<a class="btn btn-gold" href="' + app.ios + '">App Store</a>';
    if (app.android) b += '<a class="btn btn-gold" href="' + app.android + '">Google Play</a>';
    if (app.web) b += '<a class="btn btn-ghost" href="' + app.web + '">Open in browser</a>';
    b += '<a class="btn btn-ghost" href="../' + app.page + '">About ' + app.name + '</a>';
    msg.textContent = (app.ios || app.android) ? 'Choose your store.' : app.soon;
    btns.innerHTML = b;
  }

  /* Play Firefly Dash in the page (loads only after a tap) */
  function play() {
    $$('[data-play]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var f = document.createElement('iframe');
        f.src = btn.getAttribute('data-play');
        f.title = 'Firefly Dash';
        f.allow = 'autoplay; fullscreen';
        btn.replaceWith(f);
        f.focus();
      });
    });
  }

  /* Tester / launch sign-up */
  function signup() {
    $$('form.signup').forEach(function (form) {
      var msg = $('.form-msg', form), btn = $('button[type=submit]', form);
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        msg.className = 'form-msg'; msg.textContent = '';
        var email = $('input[type=email]', form).value.trim();
        var apps = $$('input[name=apps]:checked', form).map(function (i) { return i.value; });
        var device = ($('input[name=device]:checked', form) || {}).value;
        var wants = ($('input[name=wants]:checked', form) || {}).value || 'test';
        if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) { msg.className = 'form-msg err'; msg.textContent = 'Enter an email address like name@example.com.'; return; }
        if (!apps.length) { msg.className = 'form-msg err'; msg.textContent = 'Pick at least one app.'; return; }
        if (!device) { msg.className = 'form-msg err'; msg.textContent = 'Pick the phone you use.'; return; }
        btn.disabled = true; btn.textContent = 'Joining…';
        fetch(window.MOONSHIFT_SIGNUPS.url, {
          method: 'POST',
          headers: { 'apikey': window.MOONSHIFT_SIGNUPS.key, 'Content-Type': 'application/json', 'Prefer': 'return=minimal' },
          body: JSON.stringify({ email: email, apps: apps, device: device, wants: wants, source: 'website' })
        }).then(function (r) {
          if (r.ok) { form.reset(); msg.className = 'form-msg ok'; msg.textContent = "You're on the list. We'll email you when there's something to try."; return; }
          if (r.status === 409) { msg.className = 'form-msg ok'; msg.textContent = "That email is already on the list. You're all set."; return; }
          throw new Error('status ' + r.status);
        }).catch(function () {
          msg.className = 'form-msg err';
          msg.textContent = "Couldn't save your sign-up. Check your connection and try again, or email hello@moonshiftstudio.com.";
        }).then(function () { btn.disabled = false; btn.textContent = 'Join the list'; });
      });
    });
  }

  document.addEventListener('click', function (e) {
    var s = e.target.closest('[data-save-qr]');
    if (s) { saveQr(s.getAttribute('data-save-qr'), s); return; }
    var c = e.target.closest('[data-copy]');
    if (c) {
      var t = c.getAttribute('data-copy');
      try {
        navigator.clipboard.writeText(t).then(function () {
          c.textContent = 'Copied'; setTimeout(function () { c.textContent = 'Copy'; }, 1400);
        }, function () { c.textContent = 'Select and copy'; });
      } catch (err) { c.textContent = 'Select and copy'; }
    }
  });

  function boot() { header(); renderQrs(); renderStores(); runLanding(); play(); signup(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
