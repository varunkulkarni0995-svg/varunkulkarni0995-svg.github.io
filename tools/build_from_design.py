"""Turn the design canvas files (.dc.html) into plain HTML pages for GitHub Pages.
Usage: python3 tools/build_from_design.py <folder with the .dc.html files>
"""
import re, html, sys, os

P = sys.argv[1].rstrip('/') + '/'
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = {
    '/_blob/8fa8f2d89c2ed69ff295f31338b42238': '/img/layer-up-today.png',
    '/_blob/99587406297824741d5f2a549647b7d9': '/img/layer-up-window.png',
    '/_blob/8bb33d48922e9b5b5068cfcc58d5ff1a': '/img/gregory.png',
}
LINK = [('Main.dc.html', '/'), ('LayerUp.dc.html', '/layer-up.html'), ('About.dc.html', '/about.html')]

# Experience & education list (same content as the Journey design component)
ROWS = [
    ('2026–2027', 'MBA', 'Cornell Johnson · New York', 'Education', ''),
    ('[2026]', 'Executive Programme in FinTech and AI', 'IIM Calcutta (with Emeritus)', 'Certification', ''),
    ('2025', 'UPI BioAuth goes live', 'NPCI · Global Fintech Fest 2025', 'Milestone', 'PIN-less UPI with on-device biometrics; about 100 companies aligned; patent pending.'),
    ('[2025–2026]', 'Lead, Product Development · UPI', 'NPCI', '', 'Strategy for the users UPI had missed: 5M new users in 3 months.'),
    ('2023–2025', 'Lead, UPI International', 'NPCI', '', 'Success rate from ~45% to 98%.'),
    ('2021–2023', 'AePS and Aadhaar authentication', 'NPCI', '', 'Face authentication for the last mile; fraud from 1,000 to 150 cases a month.'),
    ('2021', 'Manager, Product', 'Jio Payments Bank', '', '50,000+ outlets became banking points.'),
    ('2018–2021', 'Product', 'Fino Payments Bank', '', '40+ partner integrations; success rate 96% to 98%.'),
    ('2013–2017', 'B.E., Mechanical Engineering', 'MIT Pune', 'Education', ''),
]
TAG = {'Education': '#efece5', 'Certification': '#dcefeb', 'Milestone': '#ece7fb'}


def row(r):
    when, title, org, tag, take = r
    tg = f'<span class="tag" style="background:{TAG[tag]}">{tag}</span>' if tag else ''
    tk = f'<span class="take">{html.escape(take)}</span>' if take else ''
    return (f'<li><span class="when">{when}</span><span class="what"><span class="ttl">'
            f'<strong>{html.escape(title)}</strong>{tg}</span><span class="org">{html.escape(org)}</span>{tk}</span></li>')


CAREER = '<ol class="career">' + ''.join(row(r) for r in ROWS) + '</ol>'

PAGES = [
    ('Main.dc.html', 'index.html', 'Varun Kulkarni · Product manager, builder',
     'Product manager and builder: 8.5 years building payments in India, now building independent tools in New York.'),
    ('LayerUp.dc.html', 'layer-up.html', 'Layer Up NYC · How it works · Varun Kulkarni',
     'How I built Layer Up NYC: what to wear in New York from how the weather feels.'),
    ('About.dc.html', 'about.html', 'About · Varun Kulkarni', 'About Varun Kulkarni, product manager and builder.'),
    ('NotFound.dc.html', '404.html', 'Page not found · Varun Kulkarni', 'Page not found.'),
]

for src, out, title, desc in PAGES:
    s = open(P + src).read()
    body = s[s.index('<x-dc>') + 6:s.index('</x-dc>')]
    helmet = re.search(r'<helmet>(.*?)</helmet>', body, re.S).group(1).strip()
    body = re.sub(r'<helmet>.*?</helmet>', '', body, flags=re.S)
    body = re.sub(r'<dc-import name="Journey"[^>]*></dc-import>', CAREER, body)
    for a, b in IMG.items():
        body = body.replace(a, b)
    for a, b in LINK:
        body = body.replace('href="' + a, 'href="' + b)
    head = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="stylesheet" href="/css/vk-pro.css">
<link rel="stylesheet" href="/css/bundle.css">
<link rel="stylesheet" href="/css/site.css">
{helmet}
</head>
<body>'''
    open(os.path.join(OUT, out), 'w').write(head + body + '</body>\n</html>\n')
    print('built', out)
