# Migration notes

This repository combines:

1. **The former `pages` branch of [openutau/OpenUtau](https://github.com/openutau/OpenUtau)** — the
   www.openutau.com landing page (Jekyll + [just-the-docs](https://just-the-docs.github.io/just-the-docs/)).
   Its 13 commits were flattened from `docs/` to the repo root with `git filter-repo`.
2. **The full history of the former GitHub wiki** (`OpenUtau.wiki.git`, ~800 commits) — grafted in
   under `wiki/`, then converted into Jekyll pages (front matter, `nav_*` tree, slug-compatible
   permalinks so old `github.com/.../wiki/<Page>` paths map to `/<Page>/`).

Localized wiki variants keep their old URLs but are excluded from the sidebar (`nav_exclude: true`)
and carry a "🌐 English" banner linking to their English counterpart.

## Domain

`CNAME` (www.openutau.com) was intentionally removed before the initial push to avoid stealing the
domain from the old Pages site. When cutting over:

1. Remove the custom domain from openutau/OpenUtau Pages settings.
2. Add `CNAME` file (content: `www.openutau.com`) back to this repo.
3. Add the custom domain in this repo's Pages settings.

The old `pages` branch and the original wiki are kept as fallback/archive until the cutover is
confirmed stable.

## Building locally

Requires Jekyll 4.x with `jekyll-remote-theme`, `jekyll-seo-tag`, `jekyll-feed`,
`jekyll-include-cache`:

```
jekyll serve   # http://127.0.0.1:4000
```

## Tools

`tools/convert_wiki.py` + `tools/pages_config.py` were the one-shot conversion scripts (front
matter injection and link rewriting). Kept for reference; re-running them on already-converted
files is not supported.

Cutover completed: site live at https://www.openutau.com.
