"""Write ThinkingCats blog posts"""
import pathlib

BASE = pathlib.Path('/Users/haris/Desktop/thinkingcats-landing/src/content/blog')

posts = {
    'what-is-a-large-language-model.md': r"""---
title: 'What is a large language model?'
description: 'LLMs are everywhere now. But how do they actually work? A plain-English explainer for the curious.'
pubDate: 'Mar 01 2026'
heroImage: '../../assets/blog-placeholder-1.jpg'
---

You've seen them in news headlines, product launches, and probably your own daily workflow by now. Large language models — LLMs — are the engines behind ChatGPT, Claude, Gemini, and dozens of other AI assistants. But what are they, really?

## A mathematical autocomplete

At the most basic level, an LLM is a function that predicts the next word (or more precisely, "token") given a sequence of words that came before it. Train that function on enough text — hundreds of billions of words scraped from books, websites, forums, and code repositories — and something surprising emerges: the model develops a broad, flexible understanding of language.

Not understanding in the way humans mean it. But functional understanding: it can answer questions, write code, translate languages, summarise documents, and carry on conversations.

## The architecture: Transformers

The "architecture" of virtually every major LLM today is called the **Transformer**, introduced in the landmark 2017 paper *Attention is All You Need* by researchers at Google.

The key innovation was the **attention mechanism** — a way for the model to weigh how relevant each word in the input is when predicting the next word. Instead of reading left-to-right like a human, the transformer can look at the entire context at once and decide which parts matter most.

This is why LLMs are so much better at long-context tasks than earlier models were.

## Scale changes everything

The "large" in large language model is doing a lot of work. Early neural language models had millions of parameters. GPT-3, released in 2020, had 175 billion. Today's frontier models are estimated to have over a trillion.

What researchers discovered — somewhat unexpectedly — is that as you scale up the number of parameters and the amount of training data, models don't just get *incrementally* better. They develop **emergent capabilities**: they start doing things they were never explicitly trained to do, like solving maths problems step by step, writing working code, or explaining jokes.

## What they can't do

LLMs are not databases. They don't have access to real-time information unless given tools to search the web. They can and do **hallucinate** — confidently stating untrue things, because they're optimised to produce plausible-sounding text, not verified facts.

They also have no persistent memory across conversations (unless that is explicitly built in), and they don't "think" in the way humans do — they are, at their core, extremely sophisticated pattern matching systems.

## Why it matters

Understanding LLMs at even a surface level helps you use them better, spot their mistakes faster, and think critically about the AI products being built on top of them. That's what ThinkingCats is here for.
""",

    'five-ai-tools-that-actually-save-time.md': r"""---
title: '5 AI tools that actually save time in 2026'
description: 'Cutting through the hype to find the AI tools worth adding to your daily workflow.'
pubDate: 'Mar 05 2026'
heroImage: '../../assets/blog-placeholder-2.jpg'
---

Everyone's building AI tools right now — which means a lot of noise and only a little signal. After months of testing, these are the five that have genuinely changed how I work.

## 1. Cursor (or any AI-native code editor)

If you write code, an AI-native editor has likely already saved you more hours than you realise. The point isn't autocomplete — it's the ability to describe what you want and have a capable model write a first draft that you refine. The edit loop is faster, context-aware, and increasingly impressive.

**Best for:** developers, data scientists, anyone who codes occasionally.

## 2. Perplexity

Google is slow. AI hallucinations are dangerous. Perplexity threads the needle: it's an AI search engine that cites its sources, making it fast to verify what it says. For research, background reading, and quick factual lookups, it's become my default.

**Best for:** research, fact-checking, answering "who/what/when" questions.

## 3. Whisper (via any transcription app)

OpenAI's Whisper model — available in many apps and for free via the API — transcribes audio with remarkable accuracy. Record a meeting, a voice note, or an interview. Get a transcript in seconds. The downstream uses (summaries, action items, searchable archives) are enormous.

**Best for:** meetings, interviews, podcasts, dictation.

## 4. Claude for long documents

When you need to actually *understand* a long PDF, contract, research paper, or report, Claude's extended context window is genuinely useful. Dump the whole document in, ask specific questions, request a summary structured around the points you care about.

**Best for:** lawyers, researchers, analysts, anyone who reads a lot of dense text.

## 5. Midjourney / Flux for visual mockups

Graphic design tools haven't been replaced — but the "I need a rough visual to communicate this idea" step has been dramatically shortened. For slide decks, mood boards, and fast prototyping, AI image generation is a legitimate time-saver.

**Best for:** product managers, marketers, designers who want a starting point.

---

The pattern across all of these: AI tools save time on the *first draft* — whether that's code, research, visuals, or summaries. The human is still in the loop for judgement, editing, and verification. That balance is, for now, the right one.
""",

    'how-to-publish-a-blog-post.md': r"""---
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
""",
}

for filename, content in posts.items():
    path = BASE / filename
    path.write_text(content)
    print(f"  wrote {filename}")

# Remove old placeholder posts
old_posts = [
    'first-post.md',
    'second-post.md',
    'third-post.md',
    'markdown-style-guide.md',
    'using-mdx.mdx',
]
for old in old_posts:
    p = BASE / old
    if p.exists():
        p.unlink()
        print(f"  removed {old}")

print("Done.")
