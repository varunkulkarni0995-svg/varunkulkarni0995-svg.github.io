"""Builds the website pages (v2.2) from the content below. Run: python3 tools/build_site.py"""
import html, pathlib

VERSION = "v2.4"
ROOT = pathlib.Path(__file__).resolve().parent.parent
EMAIL = "varunkulkarni0995@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/vkulkarnipm"
GITHUB = "https://github.com/varunkulkarni0995-svg"
RESUME_PDF = "/resume/Varun_Kulkarni_Resume_Web.pdf"
RESUME = "mailto:" + EMAIL + "?subject=R%C3%A9sum%C3%A9%20request"
LAYERUP = "https://varunkulkarni0995-svg.github.io/layer-up/"
APIBENCH = "https://varunkulkarni0995-svg.github.io/api-bench/"
COMPARE = APIBENCH + "compare.html"

def e(s): return html.escape(s, quote=True)

def page(title, desc, body, active=""):
    nav = [("Projects", "/#projects"), ("Experience", "/#experience"), ("About", "/about.html")]
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if n == active else ""}>{n}</a>' for n, h in nav)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<link rel="stylesheet" href="/css/vk-pro.css">
<link rel="stylesheet" href="/css/bundle.css">
<link rel="stylesheet" href="/css/site.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700;800&amp;family=Noto+Sans+Mono:wght@500;700&amp;display=swap" rel="stylesheet">
</head>
<body>
<div class="vk site">
<header class="top"><nav aria-label="Main" class="wrap navbar">
<a href="/" class="brand"><span class="mark">VK</span><span>Varun Kulkarni</span></a>
<div class="navlinks">{links}<a class="vk-btn vk-btn--secondary navcta" href="/#contact">Contact</a></div>
</nav></header>
{body}
<footer class="foot"><div class="wrap footrow">
<span class="muted">Varun Kulkarni · New York</span>
<span class="footlinks"><a href="mailto:{EMAIL}">Email</a><a href="{LINKEDIN}">LinkedIn</a><a href="{GITHUB}">GitHub</a><span class="ver">{VERSION}</span></span>
</div></footer>
</div>
</body>
</html>
"""

def rows(items):
    return "".join(f'<div class="row"><span class="vk-eyebrow">{e(k)}</span><div>{v}</div></div>' for k, v in items)

def decisions(items):
    return "".join(f'<article class="vk-card"><span class="vk-eyebrow">{e(t)}</span><h3>{e(h)}</h3><p>{e(p)}</p></article>' for t, h, p in items)

# ---------- Home ----------
impact = [
    ("UPI BioAuth", "Led PIN-less UPI payments using on-device biometrics from idea to national launch in 8 months, with about 100 banks and apps. Co-inventor on the pending patent; NPCI “Well Done” award, 2025.", "Case study coming"),
    ("UPI International", "Payment success rate rose from about 45% to 98%, and UPI payments at Indian shops for foreign visitors went live in 7 countries.", ""),
    ("UPI growth", "Led the plan for user groups UPI hadn’t yet reached: 5M new users in the first 3 months, against a 10M target.", ""),
    ("AePS fraud", "Owned how a fraud-detection model was integrated and evaluated across the platform. Fraud fell from about 1,000 to 150 cases a month.", ""),
]
experience = [
    ("Feb 2025 – May 2026", "Lead, Product Development – UPI", "NPCI", "Led UPI’s authentication strategy: on-device biometric payments, and face authentication for setting a UPI PIN. Also planned growth for user groups UPI hadn’t reached."),
    ("Apr 2023 – Jan 2025", "Lead, UPI International", "NPCI · Senior Associate from Apr 2023", "Single point of contact for NPCI and NIPL leadership; made the platform work with any foreign partner’s standard format; international transactions grew 4x in 18 months."),
    ("Jul 2021 – Mar 2023", "Senior Associate, Product Development – AePS", "NPCI", "Managed NPCI’s relationship with UIDAI, India’s national ID authority; drove face authentication to 20M+ transactions a month."),
    ("Jan 2021 – Jul 2021", "Manager, Product", "Jio Payments Bank", "Launched a banking-agent network from zero: 50,000+ shops became places to bank."),
    ("Jan 2020 – Jan 2021", "Officer, Product", "Fino Payments Bank", "Owned a banking platform that 40+ partner companies connected to through APIs; built the partner commission model."),
    ("Jan 2018 – Jan 2020", "Officer, Business Analyst", "Fino Payments Bank", "Product role on the technology team; launched an automated balance-transfer product used by 200K+ customers. “Above & Beyond Call of Duty” award, 2019."),
]
education = [
    ("2026 – 2027", "MBA (STEM-designated)", "Cornell Johnson, New York · expected May 2027", "Merit Scholarship · Fellow, Cañizares Center for Emerging Markets"),
    ("2026", "Executive Certificate Programme in FinTech and AI", "IIM Calcutta (via Emeritus)", ""),
    ("2022 – 2023", "Executive Development Program, Strategic Management", "XLRI Jamshedpur", ""),
    ("", "Certified Great People Manager", "Great Manager Institute", ""),
    ("2013 – 2017", "B.E., Mechanical Engineering", "MIT Pune", ""),
]
def career(lst):
    return '<ol class="career">' + "".join(
        f'<li><span class="when">{e(w)}</span><div class="what"><strong>{e(t)}</strong><span class="org">{e(o)}</span>{f"<span class=take>{e(x)}</span>" if x else ""}</div></li>'
        for w, t, o, x in lst) + "</ol>"

home = f"""<main>
<section class="wrap hero" aria-labelledby="hero-title">
<span class="vk-eyebrow">Varun Kulkarni · Product manager</span>
<h1 id="hero-title">I take products from idea to launch where many parties have to agree.</h1>
<p class="lede">For 8+ years I worked on payment products in India, most recently leading product development for UPI, India’s national payments network, at NPCI. I’m now in New York, studying at Cornell Johnson and building a few tools of my own.</p>
<div class="actions">
<a class="vk-btn vk-btn--primary" href="mailto:{EMAIL}">Email</a>
<a class="vk-btn vk-btn--secondary" href="{LINKEDIN}">LinkedIn</a>
<a class="vk-btn vk-btn--ghost" href="{RESUME_PDF}">Résumé (PDF)</a>
</div>
<p class="muted small">Full résumé available <a href="{RESUME}">on request</a>.</p>
<p class="muted">Open to Senior and Lead product roles in B2B, fintech and AI.</p>
</section>

<section class="band" aria-labelledby="impact-title"><div class="wrap stack">
<div><span class="vk-eyebrow">Selected impact</span><h2 id="impact-title">A few outcomes from my work</h2><p class="muted">From products I led or worked on at NPCI.</p></div>
<ul class="impact">{"".join(f'<li><strong>{e(k)}</strong><span>{e(v)}{f" <em class=muted>({e(n)})</em>" if n else ""}</span></li>' for k, v, n in impact)}</ul>
</div></section>

<section id="projects" class="wrap stack section" aria-labelledby="projects-title">
<div><span class="vk-eyebrow">Selected projects</span><h2 id="projects-title">Selected projects</h2><p class="muted">Small tools I build to stay hands-on with AI and APIs. Both are live prototypes.</p></div>
<div class="cards">
<article class="vk-card vk-card--raised proj">
<div class="shot shot--phone"><img src="/img/layer-up-today.png" alt="Layer Up NYC on a phone: feels-like 6°, an hourly strip and today's outfit"></div>
<div class="projbody">
<h3>Layer Up NYC <span class="muted thin">— a weather-based outfit planner</span></h3>
<p>Uses the forecast, how you travel and how much cold you can take to decide what to wear. Rules make the recommendation, so the same inputs always give the same result; AI only reads free-text input.</p>
<p class="muted small">Live prototype · phone · 63 unit tests, 28 browser checks</p>
<div class="actions"><a class="vk-btn vk-btn--primary" href="{LAYERUP}">Try it</a><a class="vk-btn vk-btn--ghost" href="/layer-up.html">How I built it →</a></div>
</div></article>
<article class="vk-card vk-card--raised proj">
<div class="shot"><img src="/img/api-bench-compare.png" alt="API Bench Compare Models: three AI models answer the same question side by side, with status, time and tokens for each"></div>
<div class="projbody">
<h3>API Bench <span class="muted thin">— testing APIs and comparing AI models</span></h3>
<p>Sends one prompt to several AI providers and keeps every request, response, error and timing, so the answers can be compared side by side.</p>
<p class="muted small">Live prototype · laptop · 11 AI providers</p>
<div class="actions"><a class="vk-btn vk-btn--primary" href="{COMPARE}">Try it</a><a class="vk-btn vk-btn--ghost" href="/api-bench.html">How I built it →</a></div>
</div></article>
</div>
</section>

<section class="wrap stack section" aria-labelledby="how-title">
<div><span class="vk-eyebrow">Approach</span><h2 id="how-title">How I approach product work</h2></div>
<ol class="principles">
<li><span class="vk-num">01</span><strong>Start with the people and their context</strong><span>In rural India, many farmers and workers have worn fingerprints, so fingerprint checks at village banking points often failed. I pushed banks and agents to adopt face authentication instead.</span></li>
<li><span class="vk-num">02</span><strong>Understand the whole system before changing it</strong><span>A UPI payment involves two banks, two payment providers, NPCI and the regulator. For BioAuth I mapped risk, liability and incentives for each before we chose an on-device design, and set rules for edge cases such as a user changing phone or SIM.</span></li>
<li><span class="vk-num">03</span><strong>Measure, then fix the causes</strong><span>At Fino I tracked failed transactions by cause and fixed them with partners and support teams. Transaction success rose from 96% to 98%.</span></li>
</ol>
</section>

<section id="experience" class="wrap stack section" aria-labelledby="exp-title">
<div><span class="vk-eyebrow">Experience</span><h2 id="exp-title">Experience</h2>
<p class="muted">NPCI runs India’s retail payment networks, including UPI (530M+ users nationally) and AePS, which lets people bank at village shops.</p></div>
{career(experience)}
<h2 id="edu-title" style="margin-top:32px">Education and certifications</h2>
{career(education)}
</section>

<section id="contact" class="contact" aria-labelledby="contact-title"><div class="wrap contactrow">
<div class="stack" style="gap:16px;max-width:420px"><h2 id="contact-title">Get in touch</h2><p>I’m always happy to talk about product work.</p>
<div class="actions"><a class="vk-btn invert" href="mailto:{EMAIL}">Email</a><a class="vk-btn outline" href="{LINKEDIN}">LinkedIn</a><a class="vk-btn outline" href="{RESUME_PDF}">Résumé (PDF)</a></div>
<p class="small">Full résumé available <a href="{RESUME}" style="color:#fff">on request</a>.</p></div>
<form class="cform" aria-labelledby="cform-title" onsubmit="return false">
<p id="cform-title" class="small"><strong>Contact form</strong> · coming soon. Until then, please email me.</p>
<label>Name<input class="vk-input" name="name" disabled></label>
<label>Email<input class="vk-input" name="email" type="email" disabled></label>
<label>Message<textarea class="vk-input" name="message" rows="3" disabled></textarea></label>
<button class="vk-btn invert" type="submit" disabled>Send</button>
</form>
</div></section>
</main>"""

# ---------- Build pages ----------
def build_page(back_title, badges, title, intro, buttons, img, rowsitems, decs):
    b = "".join(f'<span class="vk-badge{" vk-badge--success" if i == 0 else ""}">{e(x)}</span>' for i, x in enumerate(badges))
    btn = "".join(f'<a class="vk-btn {c}" href="{h}">{e(t)}</a>' for t, h, c in buttons)
    return f"""<main class="wrap stack page">
<a href="/#projects" class="back">← All projects</a>
<div class="badges">{b}</div>
<h1>{e(title)}</h1>
<p class="lede">{e(intro)}</p>
<div class="actions">{btn}</div>
{img}
<div class="rows">{rows(rowsitems)}</div>
<section class="stack" aria-labelledby="dec-title"><h2 id="dec-title">Product decisions and trade-offs</h2><div class="decisions">{decisions(decs)}</div></section>
</main>"""

layerup = build_page("", ["Live prototype", "Phone"], "Layer Up NYC",
    "After moving to New York, I kept dressing for the morning forecast and regretting it by evening. Layer Up plans what to wear from the hourly weather, how I’m getting around and how much cold, heat and rain I can take.",
    [("Open Layer Up", LAYERUP, "vk-btn--primary"), ("View the code on GitHub", GITHUB + "/layer-up", "vk-btn--secondary")],
    '<figure class="fig fig--phone"><img src="/img/layer-up-window.png" alt="Layer Up with 6 to 9 PM selected: coldest hour 2°, outfit hoodie and overcoat with beanie and gloves"><figcaption>Choose a time window; the app plans for the coldest hour.</figcaption></figure>',
    [("Background", e("Weather apps show the forecast, not what to wear, and they treat walking outside, the subway and a classroom the same.")),
     ("Hypothesis", e("Combining “feels like” temperature, how you travel and personal tolerance gives more useful advice than a forecast alone.")),
     ("Key decision", e("Rules choose the outfit so identical inputs give identical results and every rule can be tested. AI is reserved for reading free-text input.")),
     ("Implementation", e("Plain HTML and JavaScript on GitHub Pages; Open-Meteo for weather; Photon for place search; device location where permitted.")),
     ("Testing and validation", e("63 unit tests, 28 browser checks, and an outside review that found 2 issues, both fixed.")),
     ("Next steps", e("Planned, not built: sync across devices, a daily “layer up or down” message, and an AI chat protected by a passkey."))],
    [("Place search", "Searching for landmarks", "A search for “Times Square” matched a town called Time in Norway. I switched to Photon, which finds landmarks and ranks results near you."),
     ("Reliability", "Rules relax instead of freezing", "A review found an endless loop when the wardrobe couldn’t meet every rule. The rules now relax one step at a time, and the app says what’s missing."),
     ("Security · planned", "The AI key stays on a server", "The AI key will stay on a server, never on the phone; a passkey will unlock the chat.")])

apibench = build_page("", ["Live prototype", "Laptop", "v1.3.3"], "API Bench",
    "I built API Bench to see how APIs behave in practice, not only how their documentation describes them. Its Compare Models page sends one prompt to several AI providers side by side.",
    [("Open Compare Models", COMPARE, "vk-btn--primary"), ("Open API Bench", APIBENCH, "vk-btn--secondary"), ("View the code on GitHub", GITHUB + "/api-bench", "vk-btn--ghost")],
    '<figure class="fig"><img src="/img/api-bench-compare.png" alt="Compare Models results: three AI models answer the same question side by side, each card showing status, time, tokens and settings"><figcaption>One prompt, three providers, each with the exact request, raw response, time and tokens. (Sample run.)</figcaption></figure>',
    [("Background", e("Comparing AI models means a different console, key and format for each provider. A screenshot of a chat window doesn’t show the settings, the raw response or the timing.")),
     ("Hypothesis", e("Sending the same prompt and settings to every provider, and keeping every request and response, makes comparisons fair and repeatable.")),
     ("Key decision", e("API keys stay in the visitor’s browser, with no server in between. The trade-off: five providers that block browser calls are left out until a safe proxy exists.")),
     ("Implementation", e("Plain HTML and JavaScript on GitHub Pages. Eleven providers, including Gemini, Groq, OpenRouter, OpenAI and Anthropic. Single-turn and conversation modes; Markdown and JSON exports.")),
     ("Testing and validation", e("53 automated browser checks run before each release.")),
     ("Next steps", e("Planned: a small proxy for the blocked providers, and pass/fail scoring for answers."))],
    [("Error labels", "A setup error isn’t a model failure", "A batch-only model’s error looked like the model failing. Errors are now labelled by cause: key, rate limit, credits, unsupported model or network."),
     ("Reasoning models", "Answers lost to hidden reasoning", "Some models used their whole answer budget on hidden reasoning and returned nothing. The tool shows reasoning tokens and suggests raising the limit."),
     ("Unsupported settings", "Retry without the rejected setting", "Claude Haiku 5.5 rejects the temperature setting. The tool resends without it and keeps both attempts on record.")])

about = f"""<main class="wrap stack page narrow">
<span class="vk-eyebrow">About</span>
<h1>A little more about me</h1>
<p class="lede">I trained as a mechanical engineer and moved into product in 2018 at Fino Payments Bank. Since then I’ve worked on payments for very different users: shopkeepers acting as banking agents in villages, travellers paying abroad, and people using digital payments for the first time.</p>
<p>Most of that work was at NPCI, where a product change needs agreement from banks, apps and regulators before it ships. I enjoy that kind of problem, and I still like getting into the technical detail myself.</p>
<p>I’m now doing an MBA at Cornell Johnson in New York, where I co-founded the Cornell FinTech Club. I’ve spoken at Global Fintech Fest (2023) on UPI’s global opportunity.</p>
<h2>Outside work</h2>
<p>I’m a certified paraglider pilot and enjoy high-altitude treks, Formula 1, and old stepwells and forts.</p>
<div class="actions"><a class="vk-btn vk-btn--primary" href="mailto:{EMAIL}">Email</a><a class="vk-btn vk-btn--secondary" href="{LINKEDIN}">LinkedIn</a><a class="vk-btn vk-btn--ghost" href="/#experience">Experience and education →</a></div>
</main>"""

notfound = """<main class="wrap nf">
<div class="nfimg"><img src="/img/gregory.png" alt="Gregory, a small person peeking out of a huge rust-coloured hooded coat"></div>
<div class="stack"><span class="vk-num muted">404</span><h1>This page isn’t here. Gregory is, though.</h1><p class="lede">The link may be broken or the page may have moved.</p>
<div class="actions"><a class="vk-btn vk-btn--primary" href="/">Go home</a><a class="vk-btn vk-btn--secondary" href="/#projects">Selected projects</a></div></div>
</main>"""

pages = {
    "index.html": page("Varun Kulkarni · Product manager", "Product manager with 8+ years taking products from idea to launch, including UPI at NPCI. Now in New York.", home),
    "layer-up.html": page("Layer Up NYC · a weather-based outfit planner · Varun Kulkarni", "How I built Layer Up NYC: what to wear in New York from the hourly forecast, how you travel and your tolerance for weather.", layerup, "Projects"),
    "api-bench.html": page("API Bench · testing APIs and comparing AI models · Varun Kulkarni", "How I built API Bench: one prompt sent to several AI providers, with every request, response, error and timing kept.", apibench, "Projects"),
    "about.html": page("About Varun Kulkarni", "Product manager who moved from mechanical engineering into payments product work in India, now in New York.", about, "About"),
    "404.html": page("Page not found · Varun Kulkarni", "This page isn't here.", notfound),
}
for name, txt in pages.items():
    (ROOT / name).write_text(txt, encoding="utf-8")
print("built", ", ".join(pages))
