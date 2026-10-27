"""Verify generated output without network requests or third-party packages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent / 'docs'

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=set(); self.links=[]; self.assets=[]; self.alternates=[]
        self.h1=0; self.title=0; self.description=False; self.canonical=False; self.lang=None
    def handle_starttag(self,tag,attributes):
        a=dict(attributes)
        if 'id' in a:
            assert a['id'] not in self.ids, f'Duplicate ID {a["id"]}'
            self.ids.add(a['id'])
        if tag=='html': self.lang=a.get('lang')
        if tag=='h1': self.h1+=1
        if tag=='title': self.title+=1
        if tag=='meta' and a.get('name')=='description': self.description=bool(a.get('content'))
        if tag=='a': self.links.append(a.get('href',''))
        if tag=='a' and a.get('target')=='_blank': assert 'noopener' in a.get('rel','')
        if tag=='link' and a.get('rel')=='canonical': self.canonical=True
        if tag=='link' and a.get('rel')=='alternate': self.alternates.append(a.get('href',''))
        if tag=='script' and 'src' in a: self.assets.append(a['src'])
        if tag in ('img','source') and 'src' in a: self.assets.append(a['src'])
        if tag=='link' and a.get('rel') in ('stylesheet','icon'): self.assets.append(a.get('href',''))

def target(path):
    resolved=ROOT/unquote(path).lstrip('/')
    return resolved/'index.html' if path.endswith('/') else resolved

def main():
    pages={}
    for path in ROOT.rglob('*.html'):
        parser=Page(); parser.feed(path.read_text(encoding='utf-8')); pages[path.resolve()]=parser
        assert parser.h1==1 and parser.title==1, path
        assert parser.description and parser.canonical and parser.lang in ('ru','en'), path
    for file,page in pages.items():
        for link in page.links+page.assets+page.alternates:
            url=urlsplit(link)
            if url.scheme and url.netloc!='askardk.github.io': continue
            if url.scheme in ('mailto','tel'): continue
            dest=target(url.path) if url.path else file
            assert dest.is_file(), f'{file}: Missing {link}'
            if url.fragment:
                assert url.fragment in pages[dest.resolve()].ids, f'{file}: Missing fragment {link}'
    ElementTree.parse(ROOT/'sitemap.xml')
    assert (ROOT/'.nojekyll').exists()
    for weight in (400,600,800): assert (ROOT/f'assets/fonts/inter-{weight}.woff2').is_file()
    assert (ROOT/'assets/social-card.png').is_file()
    forbidden={'.env','.db','.sqlite','.pem','.key','.mp4','.mp3','.wav'}
    assert not [p for p in ROOT.rglob('*') if p.is_file() and p.suffix.lower() in forbidden]
    print(f'PASS: {len(pages)} pages; routes, fragments, assets, metadata, language alternates, sitemap and publication boundary.')

if __name__=='__main__': main()
