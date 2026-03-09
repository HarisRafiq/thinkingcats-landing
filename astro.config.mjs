// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://thinkingcats.com',
  integrations: [mdx(), sitemap()],
  base: '/thinkingcats-landing/', // e.g., '/my-astro-site/'

  vite: {
    plugins: [tailwindcss()],
  },
});