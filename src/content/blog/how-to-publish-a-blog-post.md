---
title: 'How to publish a new blog post on ThinkingCats'
description: 'A quick guide to adding, editing, and deploying blog content with this Astro site.'
pubDate: 'Mar 09 2026'
heroImage: '../../assets/blog-placeholder-3.jpg'
---

This site is built with [Astro](https://astro.build) and deployed to GitHub Pages via GitHub Actions. Publishing a new post is a two-step process: write the file, push to main.

## 1. Create the Markdown file

Every blog post lives in `src/content/blog/`. Create a new `.md` (or `.mdx` if you need components) file. The filename becomes part of the URL slug.

```
src/content/blog/my-new-post.md
```

Add the required frontmatter at the top:

```markdown
---
title: 'My new post'
description: 'A one-sentence description for SEO and previews.'
pubDate: 'Mar 09 2026'
heroImage: '../../assets/blog-placeholder-1.jpg'
---

Your content starts here...
```

Use standard Markdown for formatting. MDX files can import and render Astro/React components inline if needed.

## 2. Write your content

Markdown syntax works as expected:

- `# H1`, `## H2` for headings
- `**bold**`, `*italic*`
- `` `code` `` and fenced code blocks with syntax highlighting
- `[link text](url)` for links
- `![alt](image-path)` for images

For images, put them in `src/assets/` and reference with a relative path from the markdown file:

```markdown
![A diagram](../../assets/my-diagram.png)
```

Astro will optimise them automatically.

## 3. Preview locally

Run the dev server:

```bash
npm run dev
```

Visit `http://localhost:4321` to preview your changes live.

## 4. Deploy

Commit and push your changes to the `main` branch:

```bash
git add .
git commit -m "Add: my new post"
git push origin main
```

GitHub Actions will automatically build and deploy the site to GitHub Pages. The workflow file is at `.github/workflows/deploy.yml`.

## Adding a hero image

The `heroImage` field is optional but recommended. Drop an image in `src/assets/` and point to it with a relative path. Astro's image optimisation will handle resizing and converting to modern formats (WebP/AVIF).

## Adding new pages

New pages go in `src/pages/`. Create `src/pages/resources.astro` and it becomes available at `/resources`. Copy the structure of `about.astro` as a starting template.

That's it — no CMS, no build tool configuration, just Markdown and Git.
