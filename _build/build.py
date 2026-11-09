#!/usr/bin/env python3
"""Generates the static pages of royrony.github.io. Run from the repo root:
    python3 _build/build.py
Outputs index.html, games/*/index.html, privacy/index.html, 404.html,
sitemap.xml and robots.txt. Edit content here, not in the generated HTML."""
import os, html, datetime

BASE = "https://royrony.github.io"
TODAY = datetime.date.today().isoformat()
DODGE_PLAY = "https://play.google.com/store/apps/details?id=com.ronyroy.dodgestep"
SNAKE_PLAY = "https://play.google.com/store/apps/details?id=com.ronyroy.neonserpent"
DODGE_PRIV = "https://gist.github.com/royrony/a17f5e1193a2aaa230402e698faaf6c3"
DODGE_TERMS = "https://gist.github.com/royrony/2836848ec00fa641fb1f0e1177c64e61"
SNAKE_PRIV = "https://gist.github.com/royrony/682a7b3c91e2a9a50386f36f3d824446"
EMAIL = "ronyroy222@gmail.com"


def page(path, title, desc, body, depth, theme="", og="img/dodge-step/feature.jpg", nav=""):
    up = "../" * depth
    canon = BASE + "/" + path.replace("index.html", "")
    nav_items = [("Home", up or "./", "home"), ("Games", up + "#games", "games"), ("Contact", up + "#contact", "contact")]
    nav_html = "".join(
        f'<li><a href="{h}"{" aria-current=page" if k == nav else ""}>{n}</a></li>' for n, h, k in nav_items
    )
    return f"""<!doctype html>
<html lang="en" class="{theme}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#070914">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{BASE}/{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{up}favicon.png">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body class="{theme}">
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap">
<a class="brand" href="{up or './'}"><img src="{up}favicon.png" alt="" width="30" height="30">RONPIXEL</a>
<nav aria-label="Main"><ul>{nav_html}</ul></nav>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap">
<div><strong>RONPIXEL</strong><br>Small, polished Android games by Rony Roy.<br>&copy; {datetime.date.today().year} RONPIXEL</div>
<div><strong>Games</strong><ul>
<li><a href="{up}games/dodge-step/">Dodge Step</a></li>
<li><a href="{up}games/neon-serpent/">Neon Serpent</a></li></ul></div>
<div><strong>Legal</strong><ul>
<li><a href="{up}privacy/">Privacy &amp; terms</a></li>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
</div></footer>
<script src="{up}assets/site.js" defer></script>
</body>
</html>
"""


def phone(gif, still, alt):
    return f'<div class="phone"><img src="{still}" data-gif="{gif}" data-still="{still}" alt="{html.escape(alt)}" width="300" height="533"></div>'


def gallery(items):
    figs = "".join(
        f'<figure><img src="{src}" alt="{html.escape(alt)}" loading="lazy" width="230" height="408"><figcaption>{html.escape(cap)}</figcaption></figure>'
        for src, alt, cap in items
    )
    return f'<div class="gallery" role="list" aria-label="Screenshots">{figs}</div>'


def features(items):
    return '<div class="feat">' + "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in items) + "</div>"


def steps(items):
    return '<ol class="steps">' + "".join(f"<li><b>{h}</b><span>{p}</span></li>" for h, p in items) + "</ol>"


def faq(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


def ach_grid(items):
    return '<div class="ach">' + "".join(
        f'<div class="a"><img src="../../img/ach/{i}.png" alt="" width="64" height="64" loading="lazy"><b>{n}</b><span>{d}</span></div>'
        for i, n, d in items
    ) + "</div>"


# ----------------------------------------------------------------- home
def home():
    body = f"""
<section class="hero"><div class="wrap grid">
<div>
<div class="eyebrow">Indie mobile games</div>
<h1>Quick, polished games for the moments in between.</h1>
<p class="lead">RONPIXEL makes small Android games with tight controls, honest design and no accounts: play offline, chase a high score, put the phone away.</p>
<div class="cta"><a class="btn primary" href="#games">Browse games</a><a class="btn ghost" href="#about">Why RONPIXEL</a></div>
</div>
<div>{phone("img/dodge-step/gameplay.gif", "img/dodge-step/play.jpg", "Dodge Step gameplay: a runner shifting between three lanes to avoid falling shapes")}</div>
</div></section>

<section id="games"><div class="wrap">
<div class="sec-head"><h2>Games</h2><p>Free to play on Android. Each game has its own page with how to play, screenshots and leaderboard details.</p></div>
<div class="cards">
<a class="card game-card theme-dodge" href="games/dodge-step/">
<img class="cover" src="img/dodge-step/feature.jpg" alt="Dodge Step key art" width="1024" height="500">
<div class="body"><div class="row"><img src="img/dodge-step/icon-192.png" alt="" width="46" height="46"><div><h3>Dodge Step</h3><span class="pill">Arcade &middot; Reflex timing</span></div></div>
<p>Hold still. Slide at the last beat. Dodge late for bigger scores, build composure and climb the Google Play Games leaderboard.</p><span class="more">View game &rarr;</span></div></a>
<a class="card game-card theme-snake" href="games/neon-serpent/">
<img class="cover" src="img/neon-serpent/feature.jpg" alt="Neon Serpent key art" width="1024" height="500">
<div class="body"><div class="row"><img src="img/neon-serpent/icon-192.png" alt="" width="46" height="46"><div><h3>Neon Serpent: Snake Arcade</h3><span class="pill">Arcade &middot; Classic</span></div></div>
<p>The classic snake game, recharged with neon glow, combo multipliers and one-thumb swipe control. Plays fully offline.</p><span class="more">View game &rarr;</span></div></a>
</div></div></section>

<section id="about" class="alt"><div class="wrap">
<div class="sec-head"><h2>Built with a few simple rules</h2><p>Every game is held to the same standard before it ships.</p></div>
{features([
("Plays offline", "No account, no sign-up wall. Your progress lives on your device, and every game works without a connection."),
("Honest monetization", "No in-app purchases and no ads during play. Optional rewarded ads and one capped ad between runs, nothing more."),
("Smooth and responsive", "Tuned for 60 fps, instant touch feedback and safe layouts from small phones to tablets."),
("Accessible by default", "Reduced motion, larger text and high-contrast modes are built into every game."),
("Cosmetic-only rewards", "Daily streaks and achievements unlock themes and badges, never advantages, and never punish a missed day."),
("Respect for your data", "No tracking of our own. Where a Google service is used (ads, Play Games), it is disclosed in plain language."),
])}
</div></section>

<section id="contact"><div class="wrap">
<div class="sec-head"><h2>Contact</h2><p>Feedback, bug reports or press questions are welcome.</p></div>
<p><a class="btn primary" href="mailto:{EMAIL}">Email {EMAIL}</a></p>
</div></section>
"""
    return page("index.html", "RONPIXEL | Indie Android games: Dodge Step & Neon Serpent",
                "RONPIXEL makes small, polished Android games that play offline: Dodge Step and Neon Serpent.", body, 0, nav="home")


# ------------------------------------------------------------ dodge step
def dodge():
    ach = [
        ("first_run", "First Steps", "Finish your first run."),
        ("first_win", "Winner", "Win a game."),
        ("combo_5", "On a Roll", "Reach a 5x combo."),
        ("combo_7", "Unstoppable", "Reach a 7x combo."),
        ("pb_first", "Personal Best", "Beat your personal best."),
        ("runs_10", "Getting Warm", "Finish 10 runs."),
        ("runs_50", "Dedicated", "Finish 50 runs."),
        ("streak_7", "Seven-Day Spark", "Play 7 days in a row."),
    ]
    body = f"""
<section class="hero"><div class="wrap grid">
<div>
<div class="eyebrow">Arcade &middot; Reflex timing</div>
<h1>Dodge Step</h1>
<p class="lead">Hold still. Slide at the last beat. A one-thumb lane dodger scored on composure and late dodges: the later you move, the more you earn.</p>
<div class="cta"><a class="btn primary" href="{DODGE_PLAY}">Get it on Google Play</a><a class="btn ghost" href="#how">How to play</a></div>
<div class="meta"><span class="chip">Free</span><span class="chip">Plays offline</span><span class="chip">No in-app purchases</span><span class="chip">Android 7.0+</span><span class="chip">Phones &amp; tablets</span></div>
</div>
<div>{phone("../../img/dodge-step/gameplay.gif", "../../img/dodge-step/play.jpg", "Dodge Step gameplay: the avatar sidesteps falling shapes across three lanes while the score and combo climb")}</div>
</div></section>

<section id="about"><div class="wrap">
<div class="sec-head"><h2>Calm hands, sharp timing</h2>
<p>Shapes fall down three lanes. You only get a small step sideways, so the skill is waiting. Staying still while danger is on screen builds <b>Composure</b>; dodging at the very last moment scores a <b>Clutch</b>. Move too early, or twitch, and you leave points on the table.</p></div>
{features([
("Late-dodge scoring", "Every dodge is graded Early, Good, Perfect or Clutch based on how late you moved. Clutch dodges are worth ten times an Early one."),
("Composure meter", "Holding still while a threat falls fills your composure for a bigger multiplier. Twitching costs it."),
("Combo up to x7", "Chain graded dodges to build a combo multiplier. Miss the rhythm and it resets."),
("Ten rising tiers", "Speed and pressure climb every 300 points. Survive tier 10 for two seconds to earn You Win."),
("Continue once", "Reached Game Over? Watch one optional short ad to continue the same run, with your score and level kept."),
("Three themes", "Midnight, Neon and Sunset palettes, saved between sessions, plus large text, high contrast and reduced motion."),
])}
</div></section>

<section id="how" class="alt"><div class="wrap">
<div class="sec-head"><h2>How to play</h2><p>A run takes two to five minutes. The whole game is one thumb.</p></div>
{steps([
("Tap to start", "Tap anywhere on the ready screen. A short countdown, then shapes begin to fall."),
("Wait for it", "Stay still while a shape falls toward you. Your Composure meter fills, and your multiplier grows with it."),
("Slide late", "Swipe or tap the left or right half of the screen to step one lane. The closer the shape, the better the grade."),
("Chain and climb", "Keep dodging to build a combo and rise through ten tiers. Hit a shape and the run ends."),
])}
<p style="margin-top:22px;color:var(--mut)"><b>Controls:</b> swipe left/right, or tap the left/right half of the screen. On a keyboard use the arrow keys or A / D, Space or P to pause, R to restart. One lane per move, no wrap-around.</p>
</div></section>

<section id="screens"><div class="wrap">
<div class="sec-head"><h2>Screenshots</h2></div>
{gallery([
("../../img/dodge-step/menu-device.jpg", "Dodge Step main menu on an Android tablet with Leaderboard and Achievements buttons", "Menu on Android, with Play Games buttons"),
("../../img/dodge-step/play.jpg", "Gameplay with score, level and combo on screen", "Gameplay"),
("../../img/dodge-step/gameover-device.jpg", "Game Over card on a real device with a one-time Continue option", "Game Over, with one-time Continue"),
("../../img/dodge-step/achievements-device.jpg", "Google Play Games achievements list showing two of eight unlocked", "Achievements in Google Play Games"),
("../../img/dodge-step/paused.jpg", "Pause overlay with resume, settings and quit options", "Pause"),
("../../img/dodge-step/results.jpg", "Results card with score, best, combo and grade counts", "Results"),
])}
</div></section>

<section id="leaderboards" class="alt"><div class="wrap"><div class="split">
<div>
<div class="eyebrow">Google Play Games</div>
<h2>Leaderboard &amp; achievements</h2>
<p>Dodge Step is connected to Google Play Games Services. Sign in once and your best score is posted to the <b>Top Score</b> leaderboard, so you can see how you rank against friends and other players. Eight achievements unlock as you play.</p>
<ul>
<li><b>Optional:</b> the game works exactly the same if you never sign in.</li>
<li><b>Synced:</b> scores and achievements earned offline or signed out are sent the next time you are signed in.</li>
<li><b>Where to find it:</b> open the game menu and tap <b>Leaderboard</b> or <b>Achievements</b> (these appear on Android when Play Games is available).</li>
<li><b>Your data:</b> Google receives your score, achievement progress and Play Games profile name. See the <a href="{DODGE_PRIV}">privacy policy</a>.</li>
</ul>
<div class="note">The live leaderboard is shown inside the Google Play Games app and in the game itself, not on this website.</div>
</div>
<div>{ach_grid(ach)}</div>
</div></div></section>

<section id="faq"><div class="wrap">
<div class="sec-head"><h2>FAQ</h2></div>
{faq([
("Is Dodge Step free?", "Yes. There are no in-app purchases. The game shows optional rewarded ads (for the one-time Continue) and a single capped ad between runs, never during play."),
("Does it need an internet connection?", "No. The game plays fully offline. Internet is only used for ads and, if you choose to sign in, Google Play Games."),
("Will my progress be lost if I uninstall?", "Progress, best score and settings are stored on your device and are removed when you uninstall. Play Games leaderboard scores and achievements stay with your Google account."),
("Why doesn't the Leaderboard button show for me?", "The Leaderboard and Achievements buttons appear on Android devices where Google Play Games is available. Make sure Google Play Games is installed and you are signed in."),
("How do I report a bug?", f'Email <a href="mailto:{EMAIL}">{EMAIL}</a> with your device model and what happened.'),
])}
<p style="margin-top:22px"><a href="{DODGE_PRIV}">Privacy policy</a> &middot; <a href="{DODGE_TERMS}">Terms of service</a></p>
</div></section>
"""
    return page("games/dodge-step/index.html", "Dodge Step: a late-dodge arcade game for Android | RONPIXEL",
                "Dodge Step is a one-thumb lane dodger for Android. Hold still, slide at the last beat, climb the Google Play Games leaderboard. Free, offline, no in-app purchases.",
                body, 2, theme="theme-dodge", og="img/dodge-step/feature.jpg", nav="games")


# ---------------------------------------------------------- neon serpent
def snake():
    body = f"""
<section class="hero"><div class="wrap grid">
<div>
<div class="eyebrow">Arcade &middot; Classic</div>
<h1>Neon Serpent: Snake Arcade</h1>
<p class="lead">The classic snake game, recharged with arcade neon glow. Steer a glowing serpent across a midnight grid, swallow the orbs and push your high score higher.</p>
<div class="cta"><a class="btn primary" href="{SNAKE_PLAY}">Get it on Google Play</a><a class="btn ghost" href="#how">How to play</a></div>
<div class="meta"><span class="chip">Free</span><span class="chip">Plays offline</span><span class="chip">No in-app purchases</span><span class="chip">Everyone</span><span class="chip">Phones &amp; tablets</span></div>
</div>
<div>{phone("../../img/neon-serpent/gameplay.gif", "../../img/neon-serpent/play.jpg", "Neon Serpent gameplay: a glowing snake collecting orbs on a dark grid")}</div>
</div></section>

<section id="about"><div class="wrap">
<div class="sec-head"><h2>Classic snake, modern feel</h2>
<p>Fast, focused, one-thumb arcade action wrapped in a synthwave board, glowing food, punchy sound and a screen shake that lands on every bite.</p></div>
{features([
("One-thumb control", "Swipe anywhere to steer. Quick-turn buffering means fast inputs never skip or reverse. An on-screen D-pad, arrow keys and WASD are also supported."),
("Combo system", "Chain bites to build a score multiplier up to x7. Break the rhythm and it resets."),
("Rising speed", "The grid tightens with every orb. Length, speed and food count stay on screen."),
("Three neon themes", "Neon Circuit, Sunset Drive and Mint Arcade, saved between sessions."),
("Best score, always saved", "Your personal best is stored the moment a run ends. No account, no internet, no waiting."),
("Made for everyone", "Safe-area aware one-handed portrait play, large text, high contrast and a reduced-motion mode."),
])}
</div></section>

<section id="how" class="alt"><div class="wrap">
<div class="sec-head"><h2>How to play</h2></div>
{steps([
("Steer", "Swipe, press an arrow key or use the D-pad to change direction."),
("Eat", "Swallow the glowing orbs to grow your snake and score."),
("Combo", "Chain bites quickly to build a multiplier of up to x7."),
("Survive", "Never hit the wall, and never cross your own tail."),
])}
</div></section>

<section id="screens"><div class="wrap">
<div class="sec-head"><h2>Screenshots</h2></div>
{gallery([
("../../img/neon-serpent/menu.jpg", "Neon Serpent main menu", "Menu"),
("../../img/neon-serpent/play.jpg", "Gameplay with the snake, orbs and combo display", "Gameplay"),
("../../img/neon-serpent/game-over.jpg", "Game Over card with score and best", "Game Over"),
("../../img/neon-serpent/paused.jpg", "Pause overlay", "Pause"),
])}
</div></section>

<section id="leaderboards" class="alt"><div class="wrap">
<div class="sec-head"><div class="eyebrow">Google Play Games</div><h2>Leaderboard &amp; achievements</h2>
<p>A Google Play Games leaderboard and achievements for Neon Serpent are being finished. When they go live you will be able to sign in (optionally) from the menu and compare your best score with friends. This page will be updated at that point.</p></div>
</div></section>

<section id="faq"><div class="wrap">
<div class="sec-head"><h2>FAQ</h2></div>
{faq([
("Is Neon Serpent free?", "Yes. No in-app purchases. Optional rewarded ads are the only ads, and they never appear during play."),
("Does it work offline?", "Yes, fully. No account and no internet needed."),
("Is it safe for kids?", "The app is rated Everyone, but it is not designed for children under 13 and is not part of the Play Families program because it can show ads."),
("How do I report a bug?", f'Email <a href="mailto:{EMAIL}">{EMAIL}</a> with your device model and what happened.'),
])}
<p style="margin-top:22px"><a href="{SNAKE_PRIV}">Privacy policy</a></p>
</div></section>
"""
    return page("games/neon-serpent/index.html", "Neon Serpent: Snake Arcade | Classic snake game for Android | RONPIXEL",
                "Neon Serpent is the classic snake game with neon glow, combo multipliers and one-thumb swipe control. Free, offline, no in-app purchases.",
                body, 2, theme="theme-snake", og="img/neon-serpent/feature.jpg", nav="games")


# --------------------------------------------------------------- privacy
def privacy():
    body = f"""
<section><div class="wrap legal">
<div class="eyebrow">Legal</div><h1>Privacy &amp; terms</h1>
<p class="lead">Each game has its own policy because each uses slightly different services. They are hosted as public documents so Google Play and AdMob can link to them.</p>
<h2>Dodge Step</h2>
<ul><li><a href="{DODGE_PRIV}">Privacy policy</a></li><li><a href="{DODGE_TERMS}">Terms of service</a></li></ul>
<h2>Neon Serpent: Snake Arcade</h2>
<ul><li><a href="{SNAKE_PRIV}">Privacy policy</a></li></ul>
<h2>In short</h2>
<p>Games store progress on your device only. There is no account system and no analytics of our own. Google AdMob (ads) and, in Dodge Step, Google Play Games Services (leaderboard and achievements) process some data as described in each policy.</p>
<h2>Contact</h2>
<p>Questions about privacy: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>
"""
    return page("privacy/index.html", "Privacy & terms | RONPIXEL", "Privacy policies and terms of service for RONPIXEL games.", body, 1)


def notfound():
    body = """<section><div class="wrap legal"><h1>Page not found</h1><p class="lead">That page does not exist. Head back to the <a href="/">home page</a> to browse the games.</p></div></section>"""
    return page("404.html", "Page not found | RONPIXEL", "Page not found.", body, 0)


def write(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w").write(text)


if __name__ == "__main__":
    write("index.html", home())
    write("games/dodge-step/index.html", dodge())
    write("games/neon-serpent/index.html", snake())
    write("privacy/index.html", privacy())
    nf = notfound().replace('href="favicon.png"', 'href="/favicon.png"').replace('href="assets/site.css"', 'href="/assets/site.css"').replace('src="assets/site.js"', 'src="/assets/site.js"').replace('src="favicon.png"', 'src="/favicon.png"')
    write("404.html", nf)
    urls = ["", "games/dodge-step/", "games/neon-serpent/", "privacy/"]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"<url><loc>{BASE}/{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    print("built")
