import fs from 'fs';

const filepath = new URL('day1.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');
