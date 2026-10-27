"""Generate the static portfolio using only the Python standard library."""
from html import escape as esc
from pathlib import Path
import json
import shutil
from content import UI, PROJECTS, SITE, EMAIL, LINKS

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs"

def write(path, text):
    target = OUT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")

def home(lang):
    return "/" if lang == "ru" else "/en/"

def route(lang, slug):
    return home(lang) + "projects/" + slug + "/"

def arrow():
    return '<span aria-hidden="true">↗</span>'

def tags(items):
    return '<ul class="tags" aria-label="Technology">' + ''.join('<li>'+esc(item)+'</li>' for item in items) + '</ul>'

def external(url, label, css="text-link"):
    return f'<a class="{css}" href="{esc(url)}" target="_blank" rel="noopener noreferrer">{esc(label)} {arrow()}</a>'

def art(slug, lang):
    p = PROJECTS[slug]
    c = p[lang]
    labels = c["art"]
    icon = {"lumo": "✳", "kilogr": "k.", "kezen": "K"}[slug]
    if slug == "lumo":
        bars = ''.join(f'<i style="--h:{h}%"></i>' for h in [15,24,42,68,38,84,54,96,62,39,77,100,64,44,90,55,29,68,44,23,39,70,46,21])
        inner = f'''<div class="audio-window"><div class="window-top"><span class="window-dots"><i></i><i></i><i></i></span><span>Lumo / audio → insight</span><span class="signal-dot"></span></div><div class="waveform" aria-hidden="true">{bars}</div><div class="wave-caption">{esc(labels[0])} <span>WebSocket</span></div><div class="pipeline-row"><span>{esc(labels[1])}</span><b>→</b><span>{esc(labels[2])}</span></div><div class="hint-output"><span class="spark" aria-hidden="true">✳</span><div><small>AI</small><strong>{esc(labels[3])}</strong></div><span class="hint-arrow" aria-hidden="true">↗</span></div><div class="archive-output"><span aria-hidden="true">↳</span> {esc(labels[4])}</div></div>'''
    elif slug == "kilogr":
        inner = f'''<div class="health-orbit"><div class="orbit-ring ring-a"></div><div class="orbit-ring ring-b"></div><div class="orbit-center"><span>k.</span><small>{esc(labels[0])}</small></div><div class="orbit-node food"><span aria-hidden="true">◒</span>{esc(labels[1])}</div><div class="orbit-node activity"><span aria-hidden="true">↗</span>{esc(labels[2])}</div><div class="orbit-node training"><span aria-hidden="true">≋</span>{esc(labels[3])}</div><div class="orbit-node telegram"><span aria-hidden="true">➤</span>{esc(labels[4])}</div></div>'''
    else:
        inner = f'''<div class="community-map"><svg class="map-lines" viewBox="0 0 500 340" fill="none" aria-hidden="true"><path d="M80 75L250 170L425 70M90 270L250 170L410 275M250 170L250 30" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5 7"/></svg><div class="event-core"><span>K</span><small>{esc(labels[2])}</small></div><div class="map-node people"><span aria-hidden="true">◉ ◉</span>{esc(labels[0])}</div><div class="map-node interests"><span aria-hidden="true">✳</span>{esc(labels[1])}</div><div class="map-node conversation"><span aria-hidden="true">•••</span>{esc(labels[3])}</div><div class="map-node community"><span aria-hidden="true">◎</span>{esc(labels[4])}</div></div>'''
    return f'''<div class="project-art art-{slug}" role="img" aria-label="{esc(UI[lang]['diagram'])}: {esc(' → '.join(labels))}"><div class="art-header"><span class="product-mark">{icon}</span><span>{esc(p['name'])}</span><span class="art-corner">{p['number']} / SYSTEM</span></div>{inner}<div class="art-caption">{esc(UI[lang]['illustration'])}</div></div>'''

def shell(lang, path, title, description, main, alternate, case=False):
    u = UI[lang]
    h = home(lang)
    other = "en" if lang == "ru" else "ru"
    canonical = SITE + path
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light"><meta name="theme-color" content="#f8f8f4">
<title>{esc(title)}</title><meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="{other}" href="{SITE+alternate}"><link rel="alternate" hreflang="{lang}" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:locale" content="{'ru_RU' if lang=='ru' else 'en_US'}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{SITE}/assets/social-card.png"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/style.css"><script src="/assets/app.js" defer></script>
<script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@type':'Person','name':'Askar Dauletbek','url':SITE,'jobTitle':'Full-stack and AI developer','sameAs':list(LINKS.values())},ensure_ascii=False)}</script>
</head>
<body{' class="case-page"' if case else ''}>
<a class="skip-link" href="#main">{u['skip']}</a>
<header class="site-header"><div class="container header-inner">
<a class="brand" href="{h}" aria-label="{u['name']} — {u['home']}"><span class="brand-icon" aria-hidden="true">a<span>↗</span></span><span>Askar Dauletbek<span class="brand-role">Full-stack & AI developer</span></span></a>
<button class="menu-toggle" aria-expanded="false" aria-controls="main-nav" data-open-label="{u['menu']}" data-close-label="{u['close_menu']}">{u['menu']} <span aria-hidden="true">＋</span></button>
<nav id="main-nav" class="main-nav" aria-label="{'Основная навигация' if lang=='ru' else 'Main navigation'}"><a href="{h}#projects">{u['nav_projects']}</a><a href="{h}#about">{u['nav_about']}</a><a class="language-switch" href="{alternate}" lang="{other}" hreflang="{other}">{other.upper()}</a><a class="nav-contact" href="{h}#contact">{u['contact']} <span aria-hidden="true">↗</span></a></nav>
</div></header>
<main id="main">{main}</main>
<footer class="site-footer"><div class="container footer-inner"><span>© 2026 {u['footer']}</span><span>{u['footer_note']}</span><a href="{LINKS['github']}" target="_blank" rel="noopener noreferrer">GitHub ↗</a></div></footer>
<div class="toast" role="status" aria-live="polite"></div>
</body></html>'''

def project_row(slug, lang):
    p = PROJECTS[slug]
    c = p[lang]
    u = UI[lang]
    return f'''<article class="project-row project-{slug}"><div class="project-copy"><div class="project-index"><span>{p['number']}</span><span>{c['category']}</span></div><h3><a href="{route(lang,slug)}">{esc(p['name'])}</a></h3><p class="project-description">{esc(c['short'])}</p>{tags(p['stack'][:5])}<div class="project-links"><a class="text-link" href="{route(lang,slug)}">{u['case']} {arrow()}</a><span class="access-label"><span aria-hidden="true">{'◌' if p['access']=='private' else '↗'}</span> {u[p['access']]}</span></div></div><a class="art-link" href="{route(lang,slug)}" aria-label="{u['case']}: {esc(p['name'])}">{art(slug,lang)}</a></article>'''

def index_page(lang):
    u = UI[lang]
    systems = ''.join(f'<div class="system-step"><span>0{i+1}</span><strong>{esc(x)}</strong><span aria-hidden="true">↘</span></div>' for i,x in enumerate(u['system_nodes']))
    principles = ''.join(f'<article class="principle"><span class="mono">{n}</span><h3>{esc(title)}</h3><p>{esc(text)}</p></article>' for n,title,text in u['principles'])
    labs = ''.join(f'<a class="lab" href="{url}" target="_blank" rel="noopener noreferrer"><div><span class="eyebrow">{esc(tech)}</span><h3>{esc(title)}</h3><p>{esc(text)}</p></div><span class="lab-arrow" aria-hidden="true">↗</span></a>' for tech,title,text,url in u['labs'])
    main = f'''
<section class="hero container"><div class="hero-heading"><p class="eyebrow"><span class="status-dot"></span>{u['eyebrow']}</p><h1>{u['hero']}</h1></div><div class="hero-bottom"><div class="hero-intro"><p>{u['intro']}</p><a class="button button-dark" href="#projects">{u['see_work']} <span aria-hidden="true">↘</span></a></div><aside class="system-card"><div class="system-card-header"><span class="eyebrow">{u['system_label']}</span><span aria-hidden="true">✳</span></div><h2>{u['system_title']}</h2>{systems}<div class="system-note">{u['system_note']}</div></aside></div><div class="hero-baseline"><span>Python / JavaScript / Dart</span><span>Build · Connect · Refine</span><a href="{LINKS['github']}" target="_blank" rel="noopener noreferrer">@AskarDK ↗</a></div></section>
<section class="work-section container" id="projects"><div class="section-heading"><div><p class="eyebrow">01 / SELECTED WORK</p><h2>{u['selected']}</h2></div><p>{u['selected_sub']}</p></div>{''.join(project_row(slug,lang) for slug in PROJECTS)}</section>
<section class="about-section" id="about"><div class="container"><div class="about-heading"><div><p class="eyebrow">02 / {u['about_kicker']}</p><h2>{u['about_title']}</h2></div><p>{u['about_text']}</p></div><div class="principles">{principles}</div><div class="toolbox"><h3>{u['toolbox']}</h3>{tags(['Python','FastAPI','Flask','PostgreSQL','SQLAlchemy','Redis','WebSocket','JavaScript','Electron','Flutter','AI APIs','Git'])}</div></div></section>
<section class="explorations container"><div class="section-heading"><div><p class="eyebrow">03 / OPEN REPOSITORIES</p><h2>{u['explorations']}</h2></div><p>{u['explorations_sub']}</p></div><div class="labs">{labs}</div></section>
<section class="contact-section container" id="contact"><div class="contact-top"><p class="eyebrow">04 / {u['contact_kicker']}</p><span class="contact-star" aria-hidden="true">✳</span></div><h2>{u['contact_title']}</h2><div class="contact-bottom"><p>{u['contact_text']}</p><div class="contact-actions"><a class="email-link" href="mailto:{EMAIL}">{EMAIL} ↗</a><div class="social-links">{external(LINKS['telegram'],'Telegram')}{external(LINKS['linkedin'],'LinkedIn')}<button class="copy-email" data-email="{EMAIL}" data-success="{u['copied']}" data-failure="{u['copy_failed']}">{u['copy']}</button></div></div></div></section>'''
    return shell(lang, home(lang), u['name']+' — Full-stack & AI developer', u['intro'], main, home('en' if lang=='ru' else 'ru'))

def case_page(slug, lang):
    p = PROJECTS[slug]
    c = p[lang]
    u = UI[lang]
    next_slug = list(PROJECTS)[(list(PROJECTS).index(slug)+1)%len(PROJECTS)]
    actions = ''
    if p['url']:
        actions = external(p['url'], u['open_repo'] if p['access']=='public' else u['product'], 'button button-dark')
    decisions = ''.join(f'<article class="decision"><span class="mono">0{i+1}</span><div><h3>{esc(title)}</h3><p>{esc(text)}</p></div></article>' for i,(title,text) in enumerate(c['decisions']))
    flow = ''.join(f'<li><span class="mono">0{i+1}</span><strong>{esc(label)}</strong><span class="flow-arrow" aria-hidden="true">→</span></li>' for i,label in enumerate(c['flow']))
    main = f'''<section class="case-hero container"><a class="back-link" href="{home(lang)}#projects"><span aria-hidden="true">←</span> {u['back']}</a><div class="case-meta"><p class="eyebrow">{p['number']} / {c['category']}</p><span class="access-label">{u[p['access']]}</span></div><h1>{esc(p['name'])}<span>{esc(c['title'])}</span></h1><p class="case-intro">{esc(c['intro'])}</p><div class="case-actions">{actions}{tags(p['stack'])}</div>{art(slug,lang)}</section>
<section class="case-overview container"><div><p class="eyebrow">01 / {u['overview']}</p><h2>{u['challenge']}</h2><p>{esc(c['challenge'])}</p></div><div><p class="eyebrow">02 / DEVELOPMENT</p><h2>{u['contribution']}</h2><p>{esc(c['role'])}</p><ul class="contribution-list">{''.join('<li>'+esc(x)+'</li>' for x in c['contributions'])}</ul></div></section>
<section class="case-flow"><div class="container"><p class="eyebrow">03 / SYSTEM</p><h2>{u['flow']}</h2><ol class="flow-steps">{flow}</ol><p class="diagram-note">{u['diagram']}</p></div></section>
<section class="case-decisions container"><p class="eyebrow">04 / ENGINEERING</p><h2>{u['decisions']}</h2>{decisions}</section>
<section class="case-scope container"><h2>{u['scope']}</h2><p>{esc(c['scope'])}</p>{'<p>'+u['privacy_note']+'</p>' if p['access']=='private' else ''}</section>
<section class="next-project container"><div><p class="eyebrow">{u['next']}</p><a href="{route(lang,next_slug)}">{PROJECTS[next_slug]['name']} <span aria-hidden="true">↗</span></a></div><a class="text-link" href="{home(lang)}#contact">{u['contact']} {arrow()}</a></section>'''
    return shell(lang, route(lang,slug), p['name']+' — '+u['name'], c['short'], main, route('en' if lang=='ru' else 'ru',slug), case=True)

def main():
    OUT.mkdir(exist_ok=True)
    shutil.copytree(ROOT / "assets", OUT / "assets", dirs_exist_ok=True)
    urls=[]
    for lang in UI:
        index_path = "index.html" if lang=="ru" else "en/index.html"
        write(index_path,index_page(lang)); urls.append(home(lang))
        for slug in PROJECTS:
            path=route(lang,slug)
            write(path.lstrip('/')+'index.html',case_page(slug,lang)); urls.append(path)
    u=UI['ru']
    write('404.html',shell('ru','/404.html',u['not_found']+' — Askar Dauletbek',u['not_found_text'],f'<section class="container error-page"><p class="eyebrow">404</p><h1>{u["not_found"]}</h1><p>{u["not_found_text"]}</p><a class="button button-dark" href="/">{u["home"]} ↗</a></section>','/en/'))
    write('sitemap.xml','<?xml version="1.0" encoding="utf-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+SITE+x+'</loc></url>' for x in urls)+'</urlset>\n')
    write('robots.txt',f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    write('.nojekyll','')
    print(f'Built {len(urls)} pages, 404 page, sitemap and assets in {OUT}')

if __name__ == '__main__':
    main()
