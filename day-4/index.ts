/* eslint-disable no-console */
import fs from 'fs';

const filepath = new URL('day4.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');

const input = data.split('\n');

function chackIfContain(
  firstStart: number,
  firstEnd: number,
  secondStart: number,
  secondEnd: number,
): boolean {
  if (firstStart <= secondStart && firstEnd >= secondEnd) return true;

  if (secondStart <= firstStart && secondEnd >= firstEnd) return true;

  return false;
}

function chackIfOverlap(
  firstStart: number,
  firstEnd: number,
  secondStart: number,
  secondEnd: number,
): boolean {
  if (firstEnd >= secondStart && secondEnd >= firstEnd) return true;

  if (secondEnd >= firstStart && firstEnd >= secondEnd) return true;

  return false;
}

let containingSectionsCount = 0;
let overlapingSectionsCount = 0;

input.forEach((line) => {
  const [first, second] = line.split(',');
  const [firstRangeStart, firstRangeEnd] = first.split('-').map(Number);
  const [secondRangeStart, secondRangeEnd] = second.split('-').map(Number);

  // eslint-disable-next-line max-len
  containingSectionsCount += chackIfContain(firstRangeStart, firstRangeEnd, secondRangeStart, secondRangeEnd)
    ? 1 : 0;

  // eslint-disable-next-line max-len
  overlapingSectionsCount += chackIfOverlap(firstRangeStart, firstRangeEnd, secondRangeStart, secondRangeEnd)
    ? 1 : 0;
});

// part one answer
console.log(containingSectionsCount);

// part two answer
console.log(overlapingSectionsCount);
