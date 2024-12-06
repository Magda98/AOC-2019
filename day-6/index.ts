/* eslint-disable function-paren-newline */
/* eslint-disable @typescript-eslint/comma-dangle */
/* eslint-disable implicit-arrow-linebreak */
/* eslint-disable no-console */
import fs from 'fs';

const filepath = new URL('day6.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');

const labMap = data.split('\n').map((value) => value.split(''));
let x = labMap
  .find((value) => value.includes('^'))
  ?.findIndex((innerValue) => innerValue === '^') ?? 0;
let y = labMap.findIndex((value) => value.includes('^'));
const stepSet = new Set<string>();
let direction: 'up' | 'down' | 'left' | 'right' = 'up';
while (true) {
  const isObstacle = labMap[y][x] === '#';
  if (!isObstacle) stepSet.add(`${x},${y}`);
  if (isObstacle && direction === 'up') {
    y += 1;
    direction = 'right';
  } else if (isObstacle && direction === 'down') {
    y -= 1;
    direction = 'left';
  } else if (isObstacle && direction === 'left') {
    x += 1;
    direction = 'up';
  } else if (isObstacle && direction === 'right') {
    x -= 1;
    direction = 'down';
  }

  if (direction === 'up') {
    y -= 1;
  }
  if (direction === 'down') {
    y += 1;
  }
  if (direction === 'left') {
    x -= 1;
  }
  if (direction === 'right') {
    x += 1;
  }
  if (x > labMap[0].length - 1 || y > labMap.length - 1) {
    break;
  }
}

console.log('🚀 ~ steps:', stepSet.size);
