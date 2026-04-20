import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const equipment = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './content/equipment' }),
  schema: z.object({
    name: z.string(),
    category: z.string(),
    tags: z.array(z.string()),
    brand: z.string(),
    model: z.string(),
    location: z.string().optional(),
    status: z.enum(['可用', '使用中', '维修中']).default('可用'),
    image: z.string(),
    manual_pdf: z.string().optional(),
    datasheet_pdf: z.string().optional(),
    specs: z.record(z.string(), z.string()).optional(),
  }),
});

export const collections = { equipment };
