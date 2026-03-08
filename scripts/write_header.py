content = r"""---
import { SITE_TITLE } from '../consts';
import HeaderLink from './HeaderLink.astro';
---

<header>
	<nav>
		<a href="/" class="site-logo">
			<span class="logo-icon">🐱</span>
			<span>{SITE_TITLE}</span>
		</a>
		<div class="internal-links">
			<HeaderLink href="/">Home</HeaderLink>
			<HeaderLink href="/blog">Blog</HeaderLink>
			<HeaderLink href="/pricing">Pricing</HeaderLink>
			<HeaderLink href="/about">About</HeaderLink>
		</div>
	</nav>
</header>

<style>
	header {
		margin: 0;
		padding: 0 1.5em;
		background: white;
		box-shadow: 0 1px 0 rgba(0,0,0,0.08);
		position: sticky;
		top: 0;
		z-index: 50;
	}
	nav {
		display: flex;
		align-items: center;
		justify-content: space-between;
		max-width: 1100px;
		margin: 0 auto;
		height: 64px;
	}
	.site-logo {
		display: flex;
		align-items: center;
		gap: 0.5em;
		font-size: 1.15em;
		font-weight: 700;
		color: rgb(var(--black));
		text-decoration: none;
	}
	.logo-icon {
		font-size: 1.4em;
		line-height: 1;
	}
	.site-logo:hover {
		color: var(--accent);
	}
	.internal-links {
		display: flex;
		align-items: center;
		gap: 0.1em;
	}
	.internal-links a {
		padding: 0.45em 0.75em;
		color: rgb(var(--gray-dark));
		border-radius: 6px;
		text-decoration: none;
		font-size: 0.9em;
		font-weight: 500;
		transition: background 0.15s, color 0.15s;
		border-bottom: none;
	}
	.internal-links a:hover {
		background: rgb(var(--gray-light));
		color: rgb(var(--black));
	}
	.internal-links a.active {
		color: var(--accent);
		background: rgba(35,55,255,0.07);
	}
	@media (max-width: 600px) {
		.internal-links a {
			padding: 0.45em 0.4em;
			font-size: 0.8em;
		}
		.site-logo span:last-child {
			display: none;
		}
	}
</style>
"""

import os
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(base, 'src/components/Header.astro'), 'w') as f:
    f.write(content)

print("Header.astro written.")
