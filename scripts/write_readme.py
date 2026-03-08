"""Write the README"""
import pathlib, textwrap

BASE = pathlib.Path('/Users/haris/Desktop/thinkingcats-landing')

readme = textwrap.dedent(r"""
# ThinkingCats

> SEO-optimised landing page + blog for [thinkingcats.com](https://thinkingcats.com)
> Built with [Astro](https://astro.build) · Deployed free via GitHub Pages

---

## Quick start

```bash
npm install
npm run dev       # http://localhost:4321
npm run build     # production build → dist/
```

---

## Publishing a blog post

1. Create a `.md` (or `.mdx`) file in `src/content/blog/`:

```markdown
---
title: 'Your post title'
description: 'One-sentence description for SEO.'
pubDate: 'Mar 09 2026'
heroImage: '../../assets/blog-placeholder-1.jpg'
---

Your content here in Markdown...
```

2. Commit and push to `main` — GitHub Actions deploys automatically.

---

## Adding a page

Create `src/pages/your-page.astro` — it becomes available at `/your-page`.
Copy `src/pages/about.astro` as a template.

---

## Site structure

```
src/
├── components/
│   ├── BaseHead.astro      # <head> with SEO meta tags
│   ├── Header.astro        # sticky nav bar
│   ├── Footer.astro        # footer with links
│   └── FormattedDate.astro
├── content/
│   └── blog/               # ← your .md blog posts go here
├── layouts/
│   └── BlogPost.astro      # blog post wrapper layout
├── pages/
│   ├── index.astro         # landing page
│   ├── blog/               # blog index + individual post routes
│   ├── pricing.astro       # pricing page
│   └── about.astro         # about page
├── styles/
│   └── global.css          # global styles + Tailwind
└── consts.ts               # SITE_TITLE, SITE_DESCRIPTION
```

---

## Deploying to GitHub Pages (free)

### First-time setup

1. Push this repo to GitHub:
   ```bash
   git remote add origin https://github.com/YOUR_USER/thinkingcats-landing.git
   git push -u origin main
   ```
2. In GitHub → **Settings → Pages**, set **Source** to **GitHub Actions**
3. Push any commit to `main` — the action builds and deploys automatically

### Custom domain (thinkingcats.com)

The `public/CNAME` file already contains `thinkingcats.com`.
In your DNS provider, add these records:

| Type  | Name | Value               |
|-------|------|---------------------|
| A     | @    | 185.199.108.153     |
| A     | @    | 185.199.109.153     |
| A     | @    | 185.199.110.153     |
| A     | @    | 185.199.111.153     |
| CNAME | www  | YOUR_USER.github.io |

Then enable HTTPS in **Settings → Pages → Enforce HTTPS**.

---

## Key config files

| File | Purpose |
|------|---------|
| `astro.config.mjs` | Astro config, integrations (Tailwind, sitemap, MDX) |
| `src/consts.ts` | Site title and description |
| `.github/workflows/deploy.yml` | GitHub Actions deploy workflow |
| `public/CNAME` | Custom domain for GitHub Pages |

---

## Tech stack

- **Astro** — static site generator, 100 Lighthouse scores
- **Tailwind CSS v4** — utility-first styling
- **MDX** — blog posts in Markdown with optional components
- **@astrojs/sitemap** — auto-generated sitemap.xml
- **RSS** — built-in feed at `/rss.xml`
- **GitHub Actions** — free CI/CD deploy to GitHub Pages
""").lstrip()

(BASE / 'README.md').write_text(readme)
print("README written.")
