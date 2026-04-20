// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://programmlearner.github.io',
  base: '/zhu-lab-equipment',
  vite: {
    plugins: [tailwindcss()]
  }
});
