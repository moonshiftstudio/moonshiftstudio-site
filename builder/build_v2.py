"""Moonshift Studio website, v2 (premium redesign).
Builds ./site (real site for Vercel) and ./site-preview (artifact preview copy).
Edit the STORY, DEVLOG and ROADMAP lists below to update the words on the site."""
import os, shutil, html
from site_data import APPS, ICON, SOCIALS, SOCIAL_ICONS, e
from app_extra import EXTRA

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'v2')            # hand-written assets (css, js)
OUT = os.path.join(ROOT, '..', 'site')
SITE = 'https://moonshiftstudio.com'
QR_LIB = 'https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js'
FIREFLY_URL = 'https://fireflydash.moonshiftstudio.com'
BY_ID = {a['id']: a for a in APPS}
STAGE = {'nopehook': 's-nopehook', 'unbadged': 's-unbadged', 'firefly-dash': 's-firefly', 'manatable': 's-commander'}

# ---------------- words ----------------
HERO_LEDE = "I'm an overnight manager in retail. After my shift and on my days off, I build Moonshift Studio: a scam checker, a break room for workers, a one-tap game and an app for Magic players."

STORY_FIRST = "I'm an overnight manager in retail, and Moonshift Studio is what I build after my shift and on my days off."
STORY = [
    "I've always been a creative person. I make films, I do photography, and I'm a welder. Building things is my passion. I'm also great with computers and technology, so now I'm building with tech too. I went to college for cybersecurity, I know some coding, and I keep learning more from YouTube and anywhere else I can.",
    "Unbadged started with something I see all the time. A lot of companies keep people from posting about religion, politics, or anything that makes the company look bad, and people get fired for it. I wanted a place where people can talk about life and keep their jobs safe.",
    "Nopehook is about protecting people. Scams keep getting better, and it's harder than ever to tell what's real, especially for older people. I want to do what I can to help.",
    "Firefly Dash is for the fun of it. I loved Flappy Bird back in the day, and I love the kind of game that annoys you so much you can't stop playing.",
    "Manatable is the nerd in me. I play Magic: The Gathering and Dungeons & Dragons, and I hate needing a bunch of different apps for the same hobby, so I'm putting everything in one place.",
    "Right now Moonshift is one person building between shifts. My goal is to make it my full-time job, and every download, test and share gets me a little closer.",
]
HOME_STORY = [0, 5]   # which paragraphs show on the home page
PRINCIPLES = [
    ('nopehook', 'Useful first', 'Nopehook has a free tier that covers what most people need.'),
    ('unbadged', 'For working people', 'Unbadged is for the people who keep stores, warehouses and job sites running.'),
    ('firefly-dash', 'Fun that respects your time', 'Firefly Dash is quick to pick up and plays right in your browser.'),
    ('manatable', 'Built with players', 'Manatable is tested at real game nights before it launches.'),
]

DEVLOG = [  # newest first: (date label, ISO date, title, text, tags)
    ('Oct 20, 2026', '2026-10-20', 'New studio site and a testers list',
     'moonshiftstudio.com got a full redesign, with a page for every app, this devlog, and a sign-up list for anyone who wants to test apps before launch.', ['studio']),
    ('Oct 19, 2026', '2026-10-19', 'Manatable goes to game night',
     'The life counter, card scanner, deck deep dive and game night stats are now being tested at real Commander nights.', ['manatable']),
    ('Oct 17, 2026', '2026-10-17', 'Nopehook gets its name and first prototype',
     'The scam checker became Nopehook. The first working prototype checks texts, links and emails and explains the red flags in plain English.', ['nopehook']),
    ('Oct 17, 2026', '2026-10-17', 'Firefly Dash is playable on the web',
     'Firefly Dash runs in any phone browser at fireflydash.moonshiftstudio.com, with ten worlds, the Spark Shop and four-slot loadouts.', ['firefly-dash']),
    ('Oct 17, 2026', '2026-10-17', 'Moonshift Studio becomes the home for every app',
     'The studio got its name and logo. From here on, every app is published as Moonshift Studio.', ['studio']),
    ('Oct 15, 2026', '2026-10-15', 'Unbadged opens an invite-only beta',
     'Boards for every kind of job, Pay Check, group chats, DMs and Break Room Radio, open to adults 18+ by invite.', ['unbadged']),
]
ROADMAP = [
    ('Now', [('nopehook', 'Building the app from the prototype'), ('unbadged', 'Invite-only beta'),
             ('firefly-dash', 'Free to play in your browser'), ('manatable', 'Testing at game nights')]),
    ('Next', [('nopehook', 'Closed test with the testers list'), ('manatable', 'Open test on phones'),
              ('firefly-dash', 'App Store and Google Play versions')]),
    ('Later', [('nopehook', 'Launch on the App Store and Google Play'), ('unbadged', 'Public launch'),
               ('manatable', 'Launch on the App Store and Google Play')]),
]
TAG_NAMES = {'studio': 'Studio', **{a['id']: a['name'] for a in APPS}}

APP_FONTS = {
    'nopehook': 'family=Plus+Jakarta+Sans:wght@400;600;700;800',
    'unbadged': 'family=Barlow+Condensed:wght@800&family=Barlow:wght@400;600;700',
    'firefly-dash': 'family=Press+Start+2P',
    'manatable': 'family=Marcellus&family=Manrope:wght@400;600;700',
}
BASE_FONTS = 'family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..700&family=Hanken+Grotesk:wght@400..700&family=Michroma'
HOME_FONTS = BASE_FONTS + '&family=Plus+Jakarta+Sans:wght@800&family=Barlow+Condensed:wght@800&family=Press+Start+2P&family=Marcellus'

MOON_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.5 14.6A8.6 8.6 0 0 1 9.4 3.5a8.6 8.6 0 1 0 11.1 11.1z"/></svg>'
MENU_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'

def ic(app_id, cls='ic'):
    return f'<span class="{cls}">{ICON[app_id]}</span>'

def status(s):
    return f'<span class="status status-{s[0]}">{e(s[1])}</span>'

def phone(src, alt, cls=''):
    return f'<div class="phone {cls}"><div class="screen"><img src="{src}" alt="{e(alt)}" loading="lazy"></div></div>'

def page(path, title, desc, body, current='', qr=False, noindex=False, app=None, sky=False, fonts=BASE_FONTS):
    depth = path.count('/')
    r = '../' * depth
    canon = SITE + '/' + ('' if path == 'index.html' else path[:-5])
    links = [('apps', 'Apps', 'index.html#apps'), ('story', 'Story', 'story.html'), ('play', 'Play', 'index.html#play'), ('devlog', 'Devlog', 'devlog.html')]
    nav = ''.join(f'<a href="{r}{h}"{" aria-current=\"page\"" if k == current else ""}>{l}</a>' for k, l, h in links)
    nav += f'<a class="btn btn-gold" href="{r}join.html">Join the testers</a>'
    full_title = title if title.startswith('Moonshift') else f'{title} · Moonshift Studio'
    if app:
        fonts = BASE_FONTS + '&' + APP_FONTS[app]
    body_cls = ' '.join(c for c in [('app t-' + app) if app else '', 'sky' if sky else ''] if c)
    head_cls = 'head' + ('' if sky else ' always')
    applist = ''.join(f'<li><a href="{r}apps/{a["id"]}.html">{e(a["name"])}</a></li>' for a in APPS)
    follow = ''.join(f'<li><a href="{u}" rel="noopener">{lbl}</a></li>' for _, lbl, _, u in SOCIALS)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(full_title)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{e(desc)}">
{'<meta name="robots" content="noindex">' if noindex else f'<link rel="canonical" href="{canon}">'}
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}/assets/img/og.jpg">
<meta property="og:url" content="{canon}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B1427">
<link rel="icon" type="image/png" href="{r}assets/img/favicon.png">
<link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<link rel="stylesheet" href="{r}assets/ms.css">
</head>
<body{f' class="{body_cls}"' if body_cls else ''}>
<a class="skip" href="#main">Skip to content</a>
<header class="{head_cls}"><div class="wrap">
  <a class="brand" href="{r}index.html"><img src="{r}assets/img/moonshift-emblem.webp" alt="" width="38" height="38"><span>MOONSHIFT</span></a>
  <span class="clock" aria-hidden="true">{MOON_SVG}<span data-clock>10:00 PM</span></span>
  <button class="menu-btn" type="button" aria-label="Menu" aria-expanded="false" aria-controls="site-nav">{MENU_SVG}</button>
  <nav class="nav" id="site-nav" aria-label="Main">{nav}</nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="foot"><div class="wrap">
  <p class="sun">Clocked out. See you next shift.</p>
  <div class="cols">
    <div><h4>Moonshift Studio</h4><p style="max-width:34ch">Independent apps and games, built between night shifts.</p><p style="margin-top:10px">hello@moonshiftstudio.com</p></div>
    <div><h4>Apps</h4><ul>{applist}</ul></div>
    <div><h4>Studio</h4><ul><li><a href="{r}story.html">Story</a></li><li><a href="{r}devlog.html">Devlog</a></li><li><a href="{r}join.html">Join the testers</a></li><li><a href="{r}download.html">Download</a></li><li><a href="{r}contact.html">Contact</a></li><li><a href="{r}privacy.html">Privacy</a></li></ul></div>
    <div><h4>Follow</h4><ul>{follow}</ul></div>
  </div>
  <p class="legal">© 2026 Moonshift Studio. Magic: The Gathering is a trademark of Wizards of the Coast LLC. Manatable is not affiliated with, approved or endorsed by Wizards of the Coast.</p>
</div></footer>
{f'<script src="{QR_LIB}"></script>' if qr else ''}
<script src="{r}assets/ms.js"></script>
</body>
</html>
'''

def write(path, text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w').write(text)

# ---------------- shared sections ----------------
def stage(a, i, r=''):
    x = EXTRA[a['id']]
    shots = [s[0] for s in x['shots']]
    order = [shots[1], shots[0], shots[3]]
    phones = ''.join(phone(f'{r}assets/shots/{a["id"]}/{f}', f'{a["name"]} screen', f'p{k}') for k, f in enumerate(order))
    feats = ''.join(f'<li><span><b>{e(t)}.</b> {e(d)}</span></li>' for t, d in a['features'][:3])
    primary = (f'<a class="btn btn-app" href="{FIREFLY_URL}" rel="noopener">Play now</a>' if a['id'] == 'firefly-dash'
               else f'<a class="btn btn-app" href="{r}apps/{a["id"]}.html">Explore {e(a["name"])}</a>')
    second = (f'<a class="btn btn-line" href="{r}apps/{a["id"]}.html">Explore {e(a["name"])}</a>' if a['id'] == 'firefly-dash'
              else f'<a class="btn btn-line" href="{r}join.html">Test it early</a>' if a['id'] != 'unbadged'
              else f'<a class="btn btn-line" href="{r}apps/unbadged.html#get">Ask for an invite</a>')
    return f'''<article class="stage {STAGE[a["id"]]}{' flip' if i % 2 else ''}" id="{a["id"]}">
  <div class="art"><img src="{r}assets/art/{a["id"]}.webp" alt="" loading="lazy"></div>
  <div class="copy">
    <div class="name">{ic(a["id"])}{status(a["status"])}</div>
    <h3>{e(a["name"])}</h3>
    <p class="tag">{e(a["tag"])}</p>
    <p class="desc">{e(a["card"])}</p>
    <ul>{feats}</ul>
    <div class="btns">{primary}{second}</div>
  </div>
  <div class="phones" aria-hidden="true">{phones}</div>
</article>'''

def devlog_list(items):
    out = ''
    for label, iso, title, text, tags in items:
        t = ''.join(f'<span class="d-{g}"><i></i>{e(TAG_NAMES[g])}</span>' for g in tags)
        out += f'<li><time datetime="{iso}">{label}</time><div><h3>{e(title)}</h3><p>{e(text)}</p><div class="tags">{t}</div></div></li>'
    return f'<ol class="log" reversed>{out}</ol>'

def roadmap():
    lanes = ''
    for name, items in ROADMAP:
        li = ''.join(f'<li class="d-{aid}"><i></i><span><b>{e(BY_ID[aid]["name"])}</b> <span>{e(t)}</span></span></li>' for aid, t in items)
        lanes += f'<div class="lane"><h3>{name}</h3><ul>{li}</ul></div>'
    return f'<div class="road">{lanes}</div>'

def signup_form(fid):
    chips = ''.join(f'<label class="chip"><input type="checkbox" name="apps" value="{a["id"]}" id="{fid}-{a["id"]}"><span>{ic(a["id"])}{e(a["name"])}</span></label>' for a in APPS if a['id'] != 'unbadged')
    dev = ''.join(f'<label class="chip plain"><input type="radio" name="device" value="{v}" id="{fid}-dev-{v}"><span>{l}</span></label>' for v, l in [('iphone', 'iPhone'), ('android', 'Android'), ('both', 'Both')])
    wants = ''.join(f'<label class="chip plain"><input type="radio" name="wants" value="{v}" id="{fid}-w-{v}"{" checked" if v == "test" else ""}><span>{l}</span></label>' for v, l in [('test', 'Test apps before launch'), ('news', 'Just tell me when they launch')])
    return f'''<form class="signup" id="{fid}" novalidate>
  <div class="field"><label for="{fid}-email">Email</label><input type="email" id="{fid}-email" name="email" autocomplete="email" placeholder="you@example.com" required></div>
  <fieldset><legend>Which apps?</legend><div class="chips">{chips}</div></fieldset>
  <fieldset><legend>Your phone</legend><div class="chips">{dev}</div></fieldset>
  <fieldset><legend>What do you want?</legend><div class="chips">{wants}</div></fieldset>
  <div><button class="btn btn-gold" type="submit">Join the list</button></div>
  <p class="form-msg" role="status" aria-live="polite"></p>
  <p class="form-note">We only use your email to send test invites and launch news for the apps you pick. Unbadged invites are separate: email hello@unbadged.app.</p>
</form>'''

def join_block(fid):
    return f'''<div class="join">
  <div>
    <h2 class="big">Try the apps before anyone else.</h2>
    <p class="lede">Join the testers list and get early builds of Nopehook, Manatable and Firefly Dash, or just a heads-up when they launch.</p>
    <p class="callout"><b>Android testers needed.</b> Google Play asks new developers for 12 testers who keep an app for 14 days before it can launch. If you have an Android phone, you'd be a big help.</p>
  </div>
  {signup_form(fid)}
</div>'''

def play_block(preview_src):
    return f'''<div class="play">
  <div>
    <h2 class="big">Play Firefly Dash right here.</h2>
    <p class="lede">No download. Tap to fly, slip through the gaps and see how far your firefly can go.</p>
    <ul class="kbd-list">
      <li><b>Tap or click</b><span>Lift your firefly. Let go to drop.</span></li>
      <li><b>Sparks</b><span>Rare and worth grabbing. Spend them in the Spark Shop.</span></li>
      <li><b>Ten worlds</b><span>From the Moonlit Swamp to the Heart of Light at 4,200 meters.</span></li>
    </ul>
    <div class="btns"><a class="btn btn-ghost" href="{FIREFLY_URL}" rel="noopener">Open full screen</a><a class="btn btn-ghost" href="apps/firefly-dash.html">About the game</a></div>
  </div>
  <div class="phone"><div class="screen">
    <button class="poster" type="button" data-play="{preview_src}" aria-label="Play Firefly Dash here" style="background-image:url(assets/shots/firefly-dash/01-menu.webp)"><span>▶ Tap to play</span><small>Sound on for the full effect</small></button>
  </div></div>
</div>'''

def build(preview=False):
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(os.path.join(SRC, 'assets'), os.path.join(OUT, 'assets'))
    for sub in ['img', 'shots']:
        shutil.copytree(os.path.join(ROOT, 'assets-keep', sub), os.path.join(OUT, 'assets', sub))
    shutil.copytree(os.path.join(ROOT, 'assets-keep', 'art'), os.path.join(OUT, 'assets', 'art'))
    play_src = FIREFLY_URL
    if preview:
        os.makedirs(os.path.join(OUT, 'play'), exist_ok=True)
        shutil.copy(os.path.join(ROOT, 'apps-src', 'firefly', 'index.html'), os.path.join(OUT, 'play', 'firefly-dash.html'))
        play_src = 'play/firefly-dash.html'

    # ---------- home ----------
    strip = ''.join(f'<a href="#{a["id"]}">{ic(a["id"])}<span><b>{e(a["name"])}</b><small>{e(a["status"][1])}</small></span></a>' for a in APPS)
    home = f'''<section class="hero">
  <div class="hero-art"><img src="assets/art/hero.webp" alt="A crescent moon over a store parking lot at 3 AM" fetchpriority="high"></div>
  <div class="wrap">
    <h1 class="display">Made between night shifts.</h1>
    <p class="lede">{HERO_LEDE}</p>
    <div class="btns"><a class="btn btn-gold" href="#apps">See the apps</a><a class="btn btn-ghost" href="join.html">Join the testers</a></div>
  </div>
</section>
<nav class="strip" aria-label="Apps"><div class="wrap">{strip}</div></nav>
<section id="apps"><div class="wrap">
  <div class="intro"><h2 class="big">Four apps, one night shift.</h2><p class="lede">Each one started close to home: the people I work with, the people I look out for, and the friends at my game table.</p></div>
  <div class="stages">{''.join(stage(a, i) for i, a in enumerate(APPS))}</div>
</div></section>
<section id="story"><div class="wrap story">
  <figure class="portrait" style="margin:0"><img src="assets/img/moonshift-emblem.webp" alt="The Moonshift Studio emblem: a chrome M in front of a gold crescent moon" width="420" height="420" loading="lazy"><figcaption>Moonshift Studio. One person, four apps, built after the overnight shift.</figcaption></figure>
  <div class="body">
    <h2 class="big">The story</h2>
    <p class="first">{e(STORY_FIRST)}</p>
    {''.join(f'<p>{e(STORY[i])}</p>' for i in HOME_STORY)}
    <div class="btns" style="margin-top:6px"><a class="btn btn-ghost" href="story.html">Read the whole story</a></div>
  </div>
</div></section>
<section id="play"><div class="wrap">{play_block(play_src)}</div></section>
<section id="devlog"><div class="wrap split">
  <div><h2 class="big">What I've been building</h2>{devlog_list(DEVLOG[:4])}<div class="btns"><a class="btn btn-ghost" href="devlog.html">Full devlog</a></div></div>
  <div><h2 class="big">What's next</h2>{roadmap()}</div>
</div></section>
<section id="join"><div class="wrap">{join_block('join-home')}</div></section>'''
    write('index.html', page('index.html', 'Moonshift Studio', 'Moonshift Studio is a one-person studio making apps and games between night shifts: Nopehook, Unbadged, Firefly Dash and Manatable.', home, sky=True, fonts=HOME_FONTS))

    # ---------- story ----------
    why = ''.join(f'<div class="d-{aid}"><b><i></i>{e(t)}</b><p>{e(d)}</p></div>' for aid, t, d in PRINCIPLES)
    story = f'''<section class="page-head"><div class="wrap"><h1 class="display" style="max-width:12ch">Built in the hours after clock-out.</h1></div></section>
<section style="padding-top:24px"><div class="wrap story">
  <figure class="portrait" style="margin:0"><img src="assets/img/moonshift-emblem.webp" alt="The Moonshift Studio emblem" width="420" height="420"><figcaption>Moonshift Studio, est. 2026.</figcaption></figure>
  <div class="body">
    <p class="first">{e(STORY_FIRST)}</p>
    {''.join(f'<p>{e(p)}</p>' for p in STORY)}
    <p class="sig">The founder of Moonshift Studio</p>
    <div class="why">{why}</div>
  </div>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <h2 class="big">Follow along</h2>
  <p class="lede">Launches, devlogs and behind-the-scenes clips.</p>
  <div class="socials" style="margin-top:28px">{''.join(f'<a class="social" href="{u}" rel="noopener">{SOCIAL_ICONS[k]}<b>{lbl}</b><span>{h}</span></a>' for k, lbl, h, u in SOCIALS)}</div>
</div></section>'''
    write('story.html', page('story.html', 'Story', 'How Moonshift Studio started: one person building apps and games around the overnight shift.', story, 'story', sky=True))
    write('studio.html', '<!doctype html><meta charset="utf-8"><title>Story · Moonshift Studio</title><meta http-equiv="refresh" content="0; url=story.html"><link rel="canonical" href="https://moonshiftstudio.com/story"><a href="story.html">Read the Moonshift story</a>')

    # ---------- devlog ----------
    devlog = f'''<section class="page-head"><div class="wrap"><h1 class="display">Devlog</h1><p class="lede">What's new across the studio, newest first.</p></div></section>
<section style="padding-top:0"><div class="wrap split">
  <div>{devlog_list(DEVLOG)}</div>
  <div><h2>Roadmap</h2>{roadmap()}</div>
</div></section>
<section style="padding-top:0"><div class="wrap">{join_block('join-devlog')}</div></section>'''
    write('devlog.html', page('devlog.html', 'Devlog', 'Moonshift Studio devlog and roadmap: updates on Nopehook, Unbadged, Firefly Dash and Manatable.', devlog, 'devlog', sky=True))

    # ---------- join ----------
    join = f'''<section class="page-head" style="padding-bottom:0"><div class="wrap"></div></section>
<section style="padding-top:24px"><div class="wrap">{join_block('join-page')}</div></section>'''
    write('join.html', page('join.html', 'Join the testers', 'Sign up to test Moonshift Studio apps before they launch.', join, sky=True))

    # ---------- app pages ----------
    for a in APPS:
        x = EXTRA[a['id']]
        aid = a['id']
        shots = x['shots']
        ctas = ''.join(f'<a class="btn {"a-btn" if k == "gold" else "a-line"}" href="{u}" rel="noopener">{e(t)}</a>' for t, u, k in a['cta'])
        if a.get('copy'):
            ctas = f'<button class="btn a-btn" type="button" data-copy="{a["copy"]}">Copy invite email</button>' + ctas
        elif aid != 'firefly-dash':
            ctas = f'<a class="btn a-btn" href="../join.html">Test it early</a>' + ctas
        gallery = ''.join(f'<figure>{phone(f"../assets/shots/{aid}/{f}", f"{a['name']}: {t}")}<figcaption>{e(t)}<span>{e(s)}</span></figcaption></figure>' for f, t, s in shots)
        steps = ''.join(f'<li><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in x['steps'])
        feats = ''.join(f'<div><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in a['features'])
        faq = ''.join(f'<details><summary>{e(q)}</summary><p>{e(ans)}</p></details>' for q, ans in x['faq'])
        links = ''.join(
            f'<div class="contact"><span>{e(k)}</span>' + (f'<a class="addr" href="{u}" rel="noopener">{e(v)}</a>' if u else f'<span class="addr">{e(v)}</span><button class="copy" type="button" data-copy="{e(v)}">Copy</button>') + '</div>'
            for k, v, u in a['links'])
        body = f'''<section class="a-hero">
  <div class="bg"><img src="../assets/art/{aid}.webp" alt=""></div>
  <div class="wrap">
    <div>
      {ic(aid)}
      <h1>{e(a["name"])}</h1>
      <p class="tag">{e(a["tag"])}</p>
      {status(a["status"])}
      <p class="lede">{e(a["lede"])}</p>
      <div class="btns">{ctas}</div>
    </div>
    {phone(f"../assets/shots/{aid}/{shots[0][0]}", f"{a['name']}: {shots[0][1]}")}
  </div>
</section>
<section class="a-sec"><div class="wrap">
  <h2>{e(x["how"])}</h2>
  <ol class="steps">{steps}</ol>
</div></section>
<section class="a-sec" style="padding-top:0"><div class="wrap">
  <h2>Take a look</h2>
  <div class="gallery" tabindex="0" aria-label="{e(a["name"])} screenshots">{gallery}</div>
</div></section>
<section class="a-sec" style="padding-top:0"><div class="wrap">
  <h2>{e(x["feat_head"])}</h2>
  <div class="feats">{feats}</div>
  <p class="a-note">{e(a["note"])}</p>
</div></section>
<section class="a-sec" style="padding-top:0" id="get"><div class="wrap">
  <div class="get">
    <div><h2>{e(x["get_head"])}</h2><p class="sub">{e(x["get_text"])}</p></div>
    <aside class="get-card" aria-label="Get {e(a['name'])}">
      <div class="qr" data-qr="{aid}"></div>
      <p class="url">Scan with your phone camera<br>moonshiftstudio.com/get/{aid}</p>
      <div class="stores" data-stores="{aid}"></div>
      <button class="btn a-line" type="button" data-save-qr="{aid}">Save QR code</button>
    </aside>
  </div>
</div></section>
<section class="a-sec" style="padding-top:0"><div class="wrap">
  <h2>Questions</h2>
  <div class="faq">{faq}</div>
</div></section>
<section class="a-sec" style="padding-top:0"><div class="wrap">
  <h2>Find {e(a["name"])}</h2>
  <div class="contacts" style="margin-top:32px">{links}<div class="contact"><span>Privacy</span><a class="addr" href="../privacy.html#{aid}">How {e(a["name"])} handles your data</a></div></div>
</div></section>'''
        write(f'apps/{aid}.html', page(f'apps/{aid}.html', a['name'], f'{a["name"]} by Moonshift Studio. {a["tag"]} {a["card"]}', body, 'apps', qr=True, app=aid))

        landing = f'''<section class="landing"><div class="wrap" data-landing="{aid}">
  {ic(aid)}
  <h1>{e(a["name"])}</h1>
  <p id="landing-msg">Loading…</p>
  <div class="btns" id="landing-btns"><a class="btn btn-ghost" href="../apps/{aid}.html">About {e(a["name"])}</a></div>
</div></section>'''
        write(f'get/{aid}.html', page(f'get/{aid}.html', f'Get {a["name"]}', f'Get {a["name"]} by Moonshift Studio.', landing, noindex=True))

    # ---------- download ----------
    tiles = ''.join(f'''<div class="tile">
  <div class="row">{ic(a["id"])}<div><h3>{e(a["name"])}</h3>{status(a["status"])}</div></div>
  <div class="qr" data-qr="{a["id"]}"></div>
  <p class="url">moonshiftstudio.com/get/{a["id"]}</p>
  <button class="btn btn-ghost" type="button" data-save-qr="{a["id"]}">Save QR code</button>
</div>''' for a in APPS)
    download = f'''<section class="page-head"><div class="wrap"><h1 class="display">Get the apps</h1><p class="lede">Scan a code with your phone camera. It opens the right store for your phone, or the web version where there is one. The codes stay the same after launch, so they're safe to print.</p></div></section>
<section style="padding-top:24px"><div class="wrap"><div class="grid-qr">{tiles}</div></div></section>'''
    write('download.html', page('download.html', 'Get the apps', 'QR codes to download Moonshift Studio apps: Nopehook, Unbadged, Firefly Dash and Manatable.', download, qr=True))

    # ---------- contact ----------
    contacts = [('General questions', 'hello@moonshiftstudio.com'), ('Business and press', 'business@moonshiftstudio.com'),
                ('Nopehook support', 'support@nopehook.com'), ('Unbadged invites', 'hello@unbadged.app'),
                ('Unbadged safety reports', 'reports@unbadged.app'), ('Firefly Dash and Manatable', 'hello@moonshiftstudio.com')]
    cl = ''.join(f'<div class="contact"><span>{e(k)}</span><span class="addr">{e(v)}</span><button class="copy" type="button" data-copy="{e(v)}">Copy</button></div>' for k, v in contacts)
    soc = ''.join(f'<a class="social" href="{u}" rel="noopener">{SOCIAL_ICONS[k]}<b>{lbl}</b><span>{h}</span></a>' for k, lbl, h, u in SOCIALS)
    contact = f'''<section class="page-head"><div class="wrap"><h1 class="display">Get in touch</h1><p class="lede">Pick the address that fits. Every one of them reaches me.</p></div></section>
<section style="padding-top:24px"><div class="wrap"><div class="contacts">{cl}</div><div class="socials" style="margin-top:40px">{soc}</div></div></section>'''
    write('contact.html', page('contact.html', 'Contact', 'Contact Moonshift Studio: general questions, business and press, and app support.', contact))

    # ---------- privacy ----------
    privacy = open(os.path.join(ROOT, 'privacy_body.html')).read()
    write('privacy.html', page('privacy.html', 'Privacy Policy', 'How Moonshift Studio handles your information on moonshiftstudio.com and in Firefly Dash, Manatable, Unbadged and Nopehook.', privacy, sky=True))

    write('404.html', page('404.html', 'Page not found', 'This page does not exist.', '<section class="landing"><div class="wrap"><h1>Lost in the dark</h1><p>That page doesn\'t exist.</p><div class="btns"><a class="btn btn-gold" href="index.html">Back home</a></div></div></section>', noindex=True))

    write('vercel.json', '{\n  "cleanUrls": true,\n  "trailingSlash": false,\n  "redirects": [\n    { "source": "/studio", "destination": "/story", "permanent": true },\n    { "source": "/apps/commander-table", "destination": "/apps/manatable", "permanent": true },\n    { "source": "/get/commander-table", "destination": "/get/manatable", "permanent": true }\n  ]\n}\n')
    write('robots.txt', f'User-agent: *\nAllow: /\nDisallow: /get/\nSitemap: {SITE}/sitemap.xml\n')
    urls = ['', 'story', 'devlog', 'join', 'download', 'contact', 'privacy'] + [f'apps/{a["id"]}' for a in APPS]
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{SITE}/{u}</loc></url>\n' for u in urls) + '</urlset>\n')

build(preview=False)
# vercel.json belongs at the repo root (it also tells Vercel to serve ./site)
import json
_v = json.load(open(os.path.join(OUT, 'vercel.json')))
os.remove(os.path.join(OUT, 'vercel.json'))
json.dump({"outputDirectory": "site", **_v}, open(os.path.join(ROOT, '..', 'vercel.json'), 'w'), indent=2)
print('built', sum(len(f) for _, _, f in os.walk(OUT)), 'files')
