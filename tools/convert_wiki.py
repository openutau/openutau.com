#!/usr/bin/env python3
"""Convert imported GitHub-wiki markdown under wiki/ into Jekyll pages:
front matter with slug-compatible permalinks, nav tree, and rewritten links."""
import glob
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pages_config import PAGES, RETIRED

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
WIKI = os.path.join(ROOT, "wiki")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


# slug -> permalink, and normalized key -> slug
stems = [os.path.splitext(os.path.basename(f))[0] for f in glob.glob(os.path.join(WIKI, "*.md"))]
stems = [s for s in stems if s not in ("_Sidebar", "_Footer")]
by_norm = {}
for s in stems:
    by_norm[norm(s)] = s
for old, new in RETIRED.items():
    by_norm[norm(old)] = new

perm = lambda slug: "/" + slug + "/"
perm_url = lambda slug: "/" + urllib.parse.quote(slug) + "/"

LINK = re.compile(r"(!?\[[^\]]*\]\()((?:[^()\s]|\((?:[^()\s]*)\))*(?:\s+\"[^\"]*\")?)(\))")
WIKI_URL = re.compile(r"https?://github\.com/(?:stakira|openutau)/OpenUtau/wiki/")

unresolved = []


def rewrite_links(text, fname):
    text = WIKI_URL.sub("/", text)

    def repl(m):
        target = m.group(2)
        path, sep, anchor = target.partition("#")
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://|^/", path):
            return m.group(0)
        clean = urllib.parse.unquote(path)
        clean = re.sub(r"^\./|^/", "", clean).rstrip("/")
        clean = re.sub(r"\.md$", "", clean, flags=re.I)
        slug = by_norm.get(norm(clean))
        if slug is None:
            if clean:
                unresolved.append((fname, path))
            return m.group(0)
        return f"{m.group(1)}{perm_url(slug)}{sep}{anchor}{m.group(3)}"

    return LINK.sub(repl, text)


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


count = 0
for f in sorted(glob.glob(os.path.join(WIKI, "*.md"))):
    stem = os.path.splitext(os.path.basename(f))[0]
    if stem.startswith("_"):
        os.remove(f)
        print(f"removed {stem}.md")
        continue
    cfg = PAGES.get(stem)
    if cfg is None:
        print(f"!! no config for {stem}")
        continue
    text = open(f, encoding="utf-8").read()
    text = re.sub(r"^\s*---\n.*?\n---\n", "", text, count=1, flags=re.S)  # drop old front matter
    text = rewrite_links(text, stem)

    fm = ["---", f"title: {yaml_str(cfg['title'])}", f"permalink: {perm(stem)}"]
    if "lang_of" in cfg:
        fm += ["nav_exclude: true"]
    else:
        if "parent" in cfg:
            fm.append(f"parent: {yaml_str(cfg['parent'])}")
        fm.append(f"nav_order: {cfg['ord']}")
    fm.append("---\n")

    if "lang_of" in cfg:
        en = cfg["lang_of"]
        banner = f"\n> 🌐 English: [{PAGES[en]['title']}]({perm_url(en)}) · [Documentation Home](/Home/)\n"
        # insert banner after the first heading (or at top)
        hm = re.search(r"^# .*$", text, re.M)
        if hm:
            text = text[: hm.end()] + banner + text[hm.end():]
        else:
            text = banner + "\n" + text
    open(f, "w", encoding="utf-8", newline="\n").write("\n".join(fm) + text)
    count += 1

print(f"converted {count} pages")
if unresolved:
    print("UNRESOLVED links:")
    for f, l in sorted(set(unresolved)):
        print(f"  {f}: {l}")
