"""Write all ThinkingCats pages"""
import os, pathlib

BASE = pathlib.Path('/Users/haris/Desktop/thinkingcats-landing')
SRC  = BASE / 'src'

files = {}

# ── Footer ────────────────────────────────────────────────────────────────────
files['src/components/Footer.astro'] = r"""---
const today = new Date();
---

<footer>
	<div class="footer-inner">
		<div class="footer-brand">
			<a href="/" class="brand-link">🐱 ThinkingCats</a>
			<p>AI-powered insights for curious minds.</p>
		</div>
		<nav class="footer-nav">
			<div class="footer-col">
				<span class="col-title">Site</span>
				<a href="/">Home</a>
				<a href="/blog">Blog</a>
				<a href="/pricing">Pricing</a>
				<a href="/about">About</a>
			</div>
			<div class="footer-col">
				<span class="col-title">Resources</span>
				<a href="/rss.xml">RSS Feed</a>
				<a href="/sitemap-index.xml">Sitemap</a>
			</div>
		</nav>
	</div>
	<div class="footer-bottom">
		<p>&copy; {today.getFullYear()} ThinkingCats. All rights reserved.</p>
	</div>
</footer>

<style>
	footer {
		background: rgb(var(--gray-dark));
		color: rgba(255,255,255,0.75);
		margin-top: 4em;
	}
	.footer-inner {
		max-width: 1100px;
		margin: 0 auto;
		padding: 3em 1.5em 2em;
		display: flex;
		gap: 4em;
		flex-wrap: wrap;
	}
	.footer-brand {
		flex: 1;
		min-width: 200px;
	}
	.brand-link {
		font-size: 1.2em;
		font-weight: 700;
		color: white;
		text-decoration: none;
	}
	.footer-brand p {
		margin-top: 0.5em;
		font-size: 0.9em;
		line-height: 1.5;
		opacity: 0.7;
	}
	.footer-nav {
		display: flex;
		gap: 3em;
		flex-wrap: wrap;
	}
	.footer-col {
		display: flex;
		flex-direction: column;
		gap: 0.5em;
	}
	.col-title {
		font-weight: 600;
		color: white;
		font-size: 0.85em;
		text-transform: uppercase;
		letter-spacing: 0.05em;
		margin-bottom: 0.25em;
	}
	.footer-col a {
		color: rgba(255,255,255,0.65);
		text-decoration: none;
		font-size: 0.9em;
		transition: color 0.15s;
	}
	.footer-col a:hover {
		color: white;
	}
	.footer-bottom {
		border-top: 1px solid rgba(255,255,255,0.1);
		text-align: center;
		padding: 1.25em 1.5em;
		font-size: 0.85em;
		opacity: 0.6;
	}
	.footer-bottom p {
		margin: 0;
	}
</style>
"""

# ── Landing page (index.astro) ─────────────────────────────────────────────────
files['src/pages/index.astro'] = r"""---
import BaseHead from '../components/BaseHead.astro';
import Footer from '../components/Footer.astro';
import Header from '../components/Header.astro';
import { SITE_DESCRIPTION, SITE_TITLE } from '../consts';
import { getCollection } from 'astro:content';
import FormattedDate from '../components/FormattedDate.astro';

const posts = (await getCollection('blog'))
	.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf())
	.slice(0, 3);
---

<!doctype html>
<html lang="en">
	<head>
		<BaseHead title={SITE_TITLE} description={SITE_DESCRIPTION} />
	</head>
	<body>
		<Header />

		<!-- Hero -->
		<section class="hero">
			<div class="hero-inner">
				<div class="hero-badge">✨ AI + curiosity</div>
				<h1>Insights for<br /><span class="accent">curious minds</span></h1>
				<p class="hero-sub">
					ThinkingCats explores the intersection of artificial intelligence and everyday life —
					written for humans, not robots.
				</p>
				<div class="hero-cta">
					<a href="/blog" class="btn-primary">Read the blog</a>
					<a href="/pricing" class="btn-secondary">View plans</a>
				</div>
			</div>
			<div class="hero-visual" aria-hidden="true">
				<div class="cat-grid">
					<span>🐱</span><span>🤖</span><span>💡</span>
					<span>🔬</span><span>📖</span><span>🧠</span>
				</div>
			</div>
		</section>

		<!-- Features -->
		<section class="features">
			<div class="section-inner">
				<h2 class="section-title">Why ThinkingCats?</h2>
				<div class="feature-grid">
					<div class="feature-card">
						<div class="feature-icon">🎯</div>
						<h3>Focused writing</h3>
						<p>Concise, opinionated posts on AI trends, tools, and ideas — no filler.</p>
					</div>
					<div class="feature-card">
						<div class="feature-icon">🔓</div>
						<h3>Free to read</h3>
						<p>Core content is always free. Premium plans unlock deeper guides and early access.</p>
					</div>
					<div class="feature-card">
						<div class="feature-icon">⚡</div>
						<h3>Built for speed</h3>
						<p>Static Astro site — loads instantly, works offline, scores 100 on Lighthouse.</p>
					</div>
					<div class="feature-card">
						<div class="feature-icon">🔍</div>
						<h3>SEO optimised</h3>
						<p>Canonical URLs, OG tags, sitemap, and RSS feed included out of the box.</p>
					</div>
				</div>
			</div>
		</section>

		<!-- Latest posts -->
		{posts.length > 0 && (
			<section class="recent-posts">
				<div class="section-inner">
					<div class="section-header">
						<h2 class="section-title">Latest posts</h2>
						<a href="/blog" class="see-all">See all →</a>
					</div>
					<div class="post-grid">
						{posts.map(post => (
							<a href={`/blog/${post.id}/`} class="post-card">
								{post.data.heroImage && (
									<img src={post.data.heroImage.src} alt={post.data.title} class="post-thumb" width="400" height="225" />
								)}
								<div class="post-body">
									<time class="post-date"><FormattedDate date={post.data.pubDate} /></time>
									<h3>{post.data.title}</h3>
									<p>{post.data.description}</p>
								</div>
							</a>
						))}
					</div>
				</div>
			</section>
		)}

		<!-- CTA -->
		<section class="cta-section">
			<div class="cta-inner">
				<h2>Start reading today</h2>
				<p>Browse the blog or check out our plans for premium access.</p>
				<div class="cta-buttons">
					<a href="/blog" class="btn-primary">Browse articles</a>
					<a href="/pricing" class="btn-outline">See pricing</a>
				</div>
			</div>
		</section>

		<Footer />
	</body>
</html>

<style>
	/* ── Hero ── */
	.hero {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 4em;
		max-width: 1100px;
		margin: 0 auto;
		padding: 5em 1.5em 4em;
		flex-wrap: wrap;
	}
	.hero-inner {
		flex: 1;
		min-width: 280px;
		max-width: 560px;
	}
	.hero-badge {
		display: inline-block;
		background: rgba(35,55,255,0.08);
		color: var(--accent);
		border-radius: 100px;
		padding: 0.3em 0.9em;
		font-size: 0.85em;
		font-weight: 600;
		margin-bottom: 1.25em;
	}
	h1 {
		font-size: clamp(2.4em, 5vw, 3.5em);
		line-height: 1.1;
		margin-bottom: 0.6em;
	}
	.accent {
		color: var(--accent);
	}
	.hero-sub {
		font-size: 1.1em;
		color: rgb(var(--gray));
		line-height: 1.65;
		margin-bottom: 2em;
	}
	.hero-cta {
		display: flex;
		gap: 1em;
		flex-wrap: wrap;
	}
	.hero-visual {
		flex: 0 0 auto;
	}
	.cat-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 0.75em;
		font-size: 2.5em;
		line-height: 1;
		filter: grayscale(10%);
	}
	.cat-grid span {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 72px;
		height: 72px;
		background: rgb(var(--gray-light));
		border-radius: 16px;
		transition: transform 0.2s;
	}
	.cat-grid span:hover {
		transform: scale(1.1);
	}

	/* ── Buttons ── */
	.btn-primary {
		display: inline-block;
		padding: 0.7em 1.5em;
		background: var(--accent);
		color: white;
		border-radius: 8px;
		font-weight: 600;
		text-decoration: none;
		font-size: 0.95em;
		transition: opacity 0.15s, transform 0.15s;
	}
	.btn-primary:hover {
		opacity: 0.88;
		transform: translateY(-1px);
		color: white;
	}
	.btn-secondary {
		display: inline-block;
		padding: 0.7em 1.5em;
		background: rgb(var(--gray-light));
		color: rgb(var(--black));
		border-radius: 8px;
		font-weight: 600;
		text-decoration: none;
		font-size: 0.95em;
		transition: background 0.15s;
	}
	.btn-secondary:hover {
		background: rgb(var(--gray));
		color: white;
	}
	.btn-outline {
		display: inline-block;
		padding: 0.7em 1.5em;
		border: 2px solid white;
		color: white;
		border-radius: 8px;
		font-weight: 600;
		text-decoration: none;
		font-size: 0.95em;
		transition: background 0.15s;
	}
	.btn-outline:hover {
		background: rgba(255,255,255,0.15);
		color: white;
	}

	/* ── Sections ── */
	.section-inner {
		max-width: 1100px;
		margin: 0 auto;
		padding: 0 1.5em;
	}
	.section-title {
		font-size: 1.9em;
		margin-bottom: 1.5em;
	}
	.section-header {
		display: flex;
		align-items: baseline;
		justify-content: space-between;
		margin-bottom: 1.5em;
	}
	.section-header .section-title {
		margin-bottom: 0;
	}
	.see-all {
		font-weight: 600;
		color: var(--accent);
		text-decoration: none;
	}
	.see-all:hover {
		text-decoration: underline;
	}

	/* ── Features ── */
	.features {
		padding: 4em 0;
		background: rgb(var(--gray-light));
	}
	.feature-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
		gap: 1.5em;
	}
	.feature-card {
		background: white;
		border-radius: 12px;
		padding: 1.75em;
		box-shadow: var(--box-shadow);
	}
	.feature-icon {
		font-size: 2em;
		margin-bottom: 0.65em;
	}
	.feature-card h3 {
		font-size: 1.1em;
		margin-bottom: 0.5em;
	}
	.feature-card p {
		color: rgb(var(--gray));
		font-size: 0.9em;
		line-height: 1.55;
		margin: 0;
	}

	/* ── Recent posts ── */
	.recent-posts {
		padding: 4em 0;
	}
	.post-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
		gap: 1.5em;
	}
	.post-card {
		background: white;
		border: 1px solid rgb(var(--gray-light));
		border-radius: 12px;
		overflow: hidden;
		text-decoration: none;
		color: inherit;
		transition: box-shadow 0.2s, transform 0.2s;
	}
	.post-card:hover {
		box-shadow: var(--box-shadow);
		transform: translateY(-3px);
		color: inherit;
	}
	.post-thumb {
		width: 100%;
		height: 180px;
		object-fit: cover;
		border-radius: 0;
	}
	.post-body {
		padding: 1.25em 1.5em 1.5em;
	}
	.post-date {
		font-size: 0.8em;
		color: rgb(var(--gray));
		display: block;
		margin-bottom: 0.4em;
	}
	.post-body h3 {
		font-size: 1.1em;
		margin-bottom: 0.4em;
		line-height: 1.3;
	}
	.post-body p {
		font-size: 0.88em;
		color: rgb(var(--gray));
		margin: 0;
		line-height: 1.5;
		display: -webkit-box;
		-webkit-line-clamp: 3;
		-webkit-box-orient: vertical;
		overflow: hidden;
	}

	/* ── CTA ── */
	.cta-section {
		background: var(--accent);
		padding: 5em 1.5em;
		text-align: center;
		color: white;
	}
	.cta-inner {
		max-width: 600px;
		margin: 0 auto;
	}
	.cta-section h2 {
		color: white;
		font-size: 2em;
		margin-bottom: 0.5em;
	}
	.cta-section p {
		color: rgba(255,255,255,0.85);
		font-size: 1.05em;
		margin-bottom: 2em;
	}
	.cta-buttons {
		display: flex;
		gap: 1em;
		justify-content: center;
		flex-wrap: wrap;
	}
</style>
"""

# ── Pricing page ───────────────────────────────────────────────────────────────
files['src/pages/pricing.astro'] = r"""---
import BaseHead from '../components/BaseHead.astro';
import Footer from '../components/Footer.astro';
import Header from '../components/Header.astro';
import { SITE_TITLE } from '../consts';
---

<!doctype html>
<html lang="en">
	<head>
		<BaseHead
			title={`Pricing — ${SITE_TITLE}`}
			description="Simple, transparent pricing for ThinkingCats. Start free, upgrade when you need more."
		/>
	</head>
	<body>
		<Header />

		<main>
			<div class="page-hero">
				<h1>Simple pricing</h1>
				<p>Start for free. Upgrade when you're ready.</p>
			</div>

			<div class="plans">
				<!-- Free -->
				<div class="plan">
					<div class="plan-header">
						<h2>Free</h2>
						<div class="plan-price">
							<span class="price">$0</span>
							<span class="per">/ forever</span>
						</div>
					</div>
					<ul class="features">
						<li>✅ All blog posts</li>
						<li>✅ RSS feed</li>
						<li>✅ Community access</li>
						<li>❌ Premium guides</li>
						<li>❌ Early access</li>
						<li>❌ Newsletter digest</li>
					</ul>
					<a href="/blog" class="plan-cta outline">Start reading</a>
				</div>

				<!-- Pro -->
				<div class="plan featured">
					<div class="plan-badge">Most popular</div>
					<div class="plan-header">
						<h2>Pro</h2>
						<div class="plan-price">
							<span class="price">$9</span>
							<span class="per">/ month</span>
						</div>
					</div>
					<ul class="features">
						<li>✅ All blog posts</li>
						<li>✅ RSS feed</li>
						<li>✅ Community access</li>
						<li>✅ Premium guides</li>
						<li>✅ Early access to content</li>
						<li>✅ Weekly newsletter digest</li>
					</ul>
					<a href="mailto:hello@thinkingcats.com?subject=Pro plan" class="plan-cta primary">Get Pro</a>
				</div>

				<!-- Team -->
				<div class="plan">
					<div class="plan-header">
						<h2>Team</h2>
						<div class="plan-price">
							<span class="price">$39</span>
							<span class="per">/ month</span>
						</div>
					</div>
					<ul class="features">
						<li>✅ Everything in Pro</li>
						<li>✅ Up to 10 seats</li>
						<li>✅ Private Slack channel</li>
						<li>✅ Custom research requests</li>
						<li>✅ Invoice billing</li>
						<li>✅ Priority support</li>
					</ul>
					<a href="mailto:hello@thinkingcats.com?subject=Team plan" class="plan-cta outline">Contact us</a>
				</div>
			</div>

			<div class="faq">
				<h2>FAQ</h2>
				<div class="faq-list">
					<details>
						<summary>Can I cancel anytime?</summary>
						<p>Yes — cancel whenever you like with no questions asked.</p>
					</details>
					<details>
						<summary>Is there a trial period?</summary>
						<p>The Free tier lets you read all public content forever. Paid plans can be cancelled within 7 days for a full refund.</p>
					</details>
					<details>
						<summary>Do you offer discounts for students?</summary>
						<p>Yes! Email us with proof of student status and we'll set you up with 50% off Pro.</p>
					</details>
					<details>
						<summary>What payment methods do you accept?</summary>
						<p>We accept all major credit cards via Stripe. Invoicing is available on Team plans.</p>
					</details>
				</div>
			</div>
		</main>

		<Footer />
	</body>
</html>

<style>
	main {
		width: 100%;
		max-width: 1100px;
		margin: 0 auto;
		padding: 3em 1.5em;
	}
	.page-hero {
		text-align: center;
		margin-bottom: 3em;
	}
	.page-hero h1 {
		font-size: 2.8em;
		margin-bottom: 0.4em;
	}
	.page-hero p {
		font-size: 1.1em;
		color: rgb(var(--gray));
		margin: 0;
	}

	/* Plans */
	.plans {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
		gap: 1.5em;
		margin-bottom: 4em;
		align-items: start;
	}
	.plan {
		background: white;
		border: 2px solid rgb(var(--gray-light));
		border-radius: 16px;
		padding: 2em;
		position: relative;
	}
	.plan.featured {
		border-color: var(--accent);
		box-shadow: 0 0 0 4px rgba(35,55,255,0.08);
	}
	.plan-badge {
		position: absolute;
		top: -0.75em;
		left: 50%;
		transform: translateX(-50%);
		background: var(--accent);
		color: white;
		font-size: 0.78em;
		font-weight: 700;
		padding: 0.3em 0.9em;
		border-radius: 100px;
		white-space: nowrap;
	}
	.plan-header h2 {
		font-size: 1.3em;
		margin-bottom: 0.4em;
	}
	.plan-price {
		display: flex;
		align-items: baseline;
		gap: 0.25em;
		margin-bottom: 1.5em;
	}
	.price {
		font-size: 2.5em;
		font-weight: 800;
	}
	.per {
		font-size: 0.95em;
		color: rgb(var(--gray));
	}
	.features {
		list-style: none;
		padding: 0;
		margin: 0 0 2em 0;
		display: flex;
		flex-direction: column;
		gap: 0.65em;
		font-size: 0.92em;
	}
	.plan-cta {
		display: block;
		text-align: center;
		padding: 0.75em 1.5em;
		border-radius: 8px;
		font-weight: 600;
		text-decoration: none;
		font-size: 0.95em;
		transition: all 0.15s;
	}
	.plan-cta.primary {
		background: var(--accent);
		color: white;
	}
	.plan-cta.primary:hover {
		opacity: 0.88;
		color: white;
	}
	.plan-cta.outline {
		border: 2px solid rgb(var(--gray-light));
		color: rgb(var(--black));
	}
	.plan-cta.outline:hover {
		border-color: var(--accent);
		color: var(--accent);
	}

	/* FAQ */
	.faq {
		max-width: 680px;
		margin: 0 auto;
	}
	.faq h2 {
		font-size: 1.8em;
		margin-bottom: 1.25em;
		text-align: center;
	}
	.faq-list {
		display: flex;
		flex-direction: column;
		gap: 0.75em;
	}
	details {
		border: 1px solid rgb(var(--gray-light));
		border-radius: 10px;
		padding: 1em 1.25em;
	}
	summary {
		font-weight: 600;
		cursor: pointer;
		user-select: none;
		list-style: none;
		display: flex;
		justify-content: space-between;
		font-size: 0.95em;
	}
	summary::after {
		content: "+";
		font-size: 1.2em;
		line-height: 1;
		color: var(--accent);
	}
	details[open] summary::after {
		content: "−";
	}
	details p {
		margin: 0.75em 0 0;
		font-size: 0.9em;
		color: rgb(var(--gray));
		line-height: 1.6;
	}
</style>
"""

# ── About page ─────────────────────────────────────────────────────────────────
files['src/pages/about.astro'] = r"""---
import BaseHead from '../components/BaseHead.astro';
import Footer from '../components/Footer.astro';
import Header from '../components/Header.astro';
import { SITE_TITLE } from '../consts';
---

<!doctype html>
<html lang="en">
	<head>
		<BaseHead
			title={`About — ${SITE_TITLE}`}
			description="We're a small team obsessed with making AI approachable, interesting, and useful for everyday people."
		/>
	</head>
	<body>
		<Header />
		<main>
			<h1>About ThinkingCats</h1>

			<p>
				<strong>ThinkingCats</strong> is a publication exploring artificial intelligence through
				clear, honest writing. We cover tools, concepts, and ideas that matter — without the hype.
			</p>

			<h2>Our mission</h2>
			<p>
				We believe good ideas deserve clear explanations. Our goal is to make AI accessible to
				anyone curious enough to ask "how does this actually work?"
			</p>

			<h2>What we write about</h2>
			<ul>
				<li>Practical AI tools and how to use them</li>
				<li>Research papers distilled into plain English</li>
				<li>Opinions on where AI is heading</li>
				<li>Tutorials and hands-on guides</li>
			</ul>

			<h2>Get in touch</h2>
			<p>
				Have a story idea, feedback, or just want to say hi?
				Email us at <a href="mailto:hello@thinkingcats.com">hello@thinkingcats.com</a>.
			</p>
		</main>
		<Footer />
	</body>
</html>
"""

# ── Write all files ─────────────────────────────────────────────────────────────
for rel_path, content in files.items():
    full_path = BASE / rel_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content)
    print(f"  wrote {rel_path}")

print("Done.")
