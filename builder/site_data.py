"""Shared content for the Moonshift Studio website: app data, icons, socials."""
import os, shutil, html

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'site')
SITE = 'https://moonshiftstudio.com'
QR_LIB = 'https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js'

# ---------- icons ----------
ICON = {
 'nopehook': '''<svg viewBox="0 0 512 512" aria-hidden="true"><rect width="512" height="512" fill="#FFFFFF"/><g transform="translate(-8 -10)"><rect x="112" y="136" width="46" height="240" fill="#10213A"/><polygon points="112,136 170,136 267,262 267,340" fill="#10213A"/><path d="M290 136 V322 A52 52 0 0 0 394 322 V330" fill="none" stroke="#F07020" stroke-width="46"/><polygon points="417,330 417,280 394,234 346,306 371,286 371,330" fill="#F07020"/></g></svg>''',
 'unbadged': '''<svg viewBox="0 0 1024 1024" aria-hidden="true"><rect width="1024" height="1024" fill="#161B24"/><g transform="translate(112 160) scale(0.78)"><rect x="24" y="24" width="976" height="650" rx="96" fill="#1F2430" stroke="#E4E9F1" stroke-width="44"/><rect x="56" y="56" width="912" height="214" rx="64" fill="#FF7C30"/><text x="512" y="212" text-anchor="middle" font-family="'Barlow Condensed','Arial Narrow',sans-serif" font-weight="800" font-size="150" letter-spacing="10" fill="#161B24">UNBADGED</text><rect x="200" y="430" width="112" height="44" rx="22" fill="#9AA5B4"/><rect x="330" y="430" width="112" height="44" rx="22" fill="#9AA5B4"/><rect x="460" y="430" width="112" height="44" rx="22" fill="#9AA5B4"/><rect x="590" y="430" width="112" height="44" rx="22" fill="#9AA5B4"/><rect x="720" y="430" width="100" height="44" rx="22" fill="#9AA5B4"/></g></svg>''',
 'firefly-dash': None,  # built below
 'manatable': '''<svg viewBox="0 0 100 100" aria-hidden="true"><defs><linearGradient id="ctbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#221D14"/><stop offset="1" stop-color="#080706"/></linearGradient><linearGradient id="ctgold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7DE9A"/><stop offset=".5" stop-color="#C9962E"/><stop offset="1" stop-color="#F2CF7A"/></linearGradient></defs><rect width="100" height="100" fill="url(#ctbg)"/><circle cx="50" cy="50" r="33" fill="none" stroke="url(#ctgold)" stroke-width="4"/><circle cx="50" cy="50" r="26" fill="none" stroke="#7D7A73" stroke-width="1"/><circle cx="50" cy="31" r="6" fill="#F3E6BE"/><circle cx="68" cy="44" r="6" fill="#3F86D6"/><circle cx="61" cy="65" r="6" fill="#4A4A4F"/><circle cx="39" cy="65" r="6" fill="#D2463A"/><circle cx="32" cy="44" r="6" fill="#3E9A5B"/></svg>''',
}
FF = ["................",
      "................",
      "......ww.ww.....",
      ".....wwwwwww....",
      "......wwwww.....",
      ".......bbbbe....",
      ".....bbbbbbbb...",
      "...gggbbbbbbb...",
      "..gyyygbbbbb....",
      "..gyyyg.........",
      "...ggg..........",
      "................"]
COL = {'w': '#D7ECFF', 'b': '#3A2E56', 'e': '#FFFFFF', 'g': '#C6F24E', 'y': '#F7FFC9'}
px = ''.join(f'<rect x="{c}" y="{r+2}" width="1.02" height="1.02" fill="{COL[ch]}"/>' for r, row in enumerate(FF) for c, ch in enumerate(row) if ch != '.')
ICON['firefly-dash'] = f'''<svg viewBox="0 0 16 16" shape-rendering="crispEdges" aria-hidden="true"><defs><radialGradient id="ffglow" cx=".28" cy=".62" r=".45"><stop offset="0" stop-color="#C6F24E" stop-opacity=".55"/><stop offset="1" stop-color="#C6F24E" stop-opacity="0"/></radialGradient></defs><rect width="16" height="16" fill="#0B1626"/><rect width="16" height="16" fill="url(#ffglow)"/><rect x="12" y="2" width=".6" height=".6" fill="#fff"/><rect x="3" y="3" width=".5" height=".5" fill="#fff" opacity=".7"/><rect x="13" y="12" width=".5" height=".5" fill="#fff" opacity=".6"/>{px}</svg>'''

SOCIAL_ICONS = {
 'instagram': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
 'tiktok': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5"/><path d="M14 3c.5 2.8 2.4 4.6 5 4.8"/></svg>',
 'youtube': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10 9.2v5.6l4.8-2.8z" fill="currentColor" stroke="none"/></svg>',
}

# ---------- content ----------
APPS = [
 {'id': 'nopehook', 'name': 'Nopehook', 'tag': 'Check it before you bite.', 'status': ('dev', 'In development'),
  'card': 'Paste a sketchy text, email, link or screenshot and get a clear answer: likely scam, suspicious, or looks fine, with the red flags explained in plain English.',
  'lede': 'Nopehook is a scam checker for real life. Paste a text, an email, a link or a screenshot, and get a clear verdict with the warning signs spelled out and what to do next. Built for everyone, and especially for families looking out for each other.',
  'features': [
    ('Clear verdicts', 'Likely scam, suspicious, or looks fine, with the red flags explained in plain English and the next step to take.'),
    ('Built on official warnings', 'Checks are grounded in public scam alerts from agencies like the FTC and FBI, and the scam list updates every week.'),
    ('Links checked too', 'Web addresses in a message are checked against known dangerous sites before you tap them.'),
    ('Family protection', 'Look out for parents and loved ones: get an alert when someone you protect runs into a likely scam.'),
    ('Email forwarding', 'Forward a suspicious email and Nopehook checks the sender and the message for you.'),
    ('Free to start', '15 free checks every month for texts, links and screenshots.'),
  ],
  'note': 'Every result is a risk assessment, not a guarantee. When something feels off, contact the company directly using a number or website you already trust.',
  'cta': [('Follow on Instagram', 'https://instagram.com/nopehook', 'line'), ('YouTube', 'https://youtube.com/@nopehook', 'line')],
  'links': [('Instagram', '@nopehook', 'https://instagram.com/nopehook'), ('YouTube', '@nopehook', 'https://youtube.com/@nopehook'), ('Support', 'support@nopehook.com', None)]},
 {'id': 'unbadged', 'name': 'Unbadged', 'tag': 'Say it without the name tag.', 'status': ('beta', 'Invite-only beta'),
  'card': 'An anonymous break room for retail, warehouse, trades and service workers. Vent, compare pay and swap stories with people who get it.',
  'lede': 'Unbadged is an anonymous community for retail, warehouse, trades and service workers. Talk about the job, the pay and the people with others who actually get it. No real names, no tracking. Adults 18+.',
  'features': [
    ('Boards for every job', 'Boards by job type and company, each with General, Vent and Pay & Schedules chats.'),
    ('Pay Check', 'See what a job really pays, using public pay data adjusted by what members report.'),
    ('Anonymous by design', 'No real names. Faces in public photos are blurred automatically before anyone sees them.'),
    ('Group chats and DMs', 'Private group chats, and direct messages only after you both follow each other.'),
    ('Break Room Radio', 'Rock, country, rap, metal and pop stations to keep you company on break.'),
    ('Made for phones', 'Fits every screen, with pull to refresh and a text size setting.'),
  ],
  'note': 'Unbadged is in an invite-only beta for adults 18 and older. To ask for an invite, email hello@unbadged.app.',
  'cta': [('Follow on Instagram', 'https://instagram.com/unbadged', 'line')],
  'copy': 'hello@unbadged.app',
  'links': [('Instagram', '@unbadged', 'https://instagram.com/unbadged'), ('YouTube', '@joinunbadged', 'https://youtube.com/@joinunbadged'), ('Invites', 'hello@unbadged.app', None), ('Safety reports', 'reports@unbadged.app', None)]},
 {'id': 'firefly-dash', 'name': 'Firefly Dash', 'tag': 'One tap. Ten worlds.', 'status': ('live', 'Play free now'),
  'card': 'A one-tap pixel art flyer. Guide a firefly through ten glowing worlds, collect sparks and build your loadout of abilities.',
  'lede': 'Firefly Dash is a one-tap pixel art game. Tap to fly a firefly through the gaps, collect rare sparks, and push deeper through ten worlds, from the Moonlit Swamp all the way to the Heart of Light.',
  'features': [
    ('Ten worlds', 'From the Moonlit Swamp at the start to the Heart of Light at 4,200 meters, each with its own look and sound.'),
    ('New course every run', 'Courses are generated fresh each time, so no two runs are the same.'),
    ('Spark Shop', 'Spend the sparks you collect on power-ups, upgrades and glows.'),
    ('Abilities and loadouts', 'Eight abilities with a four-slot loadout, and new ones unlock as you reach new worlds.'),
    ('Plays on any phone', 'Runs right in your phone browser. Add it to your home screen to play like an app.'),
    ('One-hand friendly', 'Left- or right-hand layouts and three sound styles.'),
  ],
  'note': 'Firefly Dash is free to play in your phone browser now. App Store and Google Play versions come later.',
  'cta': [('Play now', 'https://fireflydash.moonshiftstudio.com', 'gold')],
  'links': [('Play', 'fireflydash.moonshiftstudio.com', 'https://fireflydash.moonshiftstudio.com'), ('TikTok', '@moonshiftstudio', 'https://tiktok.com/@moonshiftstudio'), ('Support', 'hello@moonshiftstudio.com', None)]},
 {'id': 'manatable', 'name': 'Manatable', 'tag': 'Collect, build and battle.', 'status': ('dev', 'In testing'),
  'card': 'Scan your cards, track life and commander damage, and see which decks you can build from what you already own.',
  'lede': 'Manatable brings a Commander game night into one app: scan your collection with your phone camera, keep life and commander damage, save every game, and dig into your decks.',
  'features': [
    ('Camera scanner', 'Point your phone at a card and it reads the name and printing, then adds it to your collection.'),
    ('Life counter', 'Life, commander damage and counters for two to six players, with each seat showing its commander.'),
    ('Game night stats', 'Finished games save automatically, with win rates, favorite commanders and rivalries.'),
    ('Deck deep dive', 'Card types, mana curve, draw odds and a coach that suggests swaps and cards to add.'),
    ('Build from what you own', 'Find commanders you can build from cards already in your collection, and what it costs to finish.'),
    ('Collection value', 'See what your cards are worth, spot valuable cards sitting in bulk, and watch prices.'),
  ],
  'note': 'Manatable is not affiliated with, approved or endorsed by Wizards of the Coast. Magic: The Gathering is a trademark of Wizards of the Coast LLC.',
  'cta': [('Follow on TikTok', 'https://tiktok.com/@moonshiftstudio', 'line')],
  'links': [('TikTok', '@moonshiftstudio', 'https://tiktok.com/@moonshiftstudio'), ('Contact', 'hello@moonshiftstudio.com', None)]},
]
SOCIALS = [('instagram', 'Instagram', '@moonshiftstudio', 'https://instagram.com/moonshiftstudio'),
           ('tiktok', 'TikTok', '@moonshiftstudio', 'https://tiktok.com/@moonshiftstudio'),
           ('youtube', 'YouTube', '@moonshiftstudio', 'https://youtube.com/@moonshiftstudio')]
e = html.escape

def icon(app_id, cls='app-icon'):
    return f'<div class="{cls}">{ICON[app_id]}</div>'

def status(s):
    return f'<span class="status status-{s[0]}">{e(s[1])}</span>'

