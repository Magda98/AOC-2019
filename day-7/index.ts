/* eslint-disable no-console */
import fs from 'fs';
import { sortBy, values } from 'lodash-es';

const filepath = new URL('day7.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');
const input = data.split('\n');

const path: string[] = [];
let directorySum: Record<string, number> = {};

input.forEach((line, index) => {
  const [first, second, third] = line.split(' ');

  if (first === '$' && second === 'cd' && third !== '..') {
    // set unique folder name
    const key = third + index;

    directorySum = { ...directorySum, [key]: 0 };
    path.push(key);
  } else if (first === '$' && second === 'cd' && third === '..') {
    path.pop();
  } else if (first !== '$' && first !== 'dir' && third === undefined) {
    const count = Number(first);
    path.forEach((key) => {
      directorySum[key] += count;
    });
  }
});

const arrayOfValues = values(directorySum);
const sum = arrayOfValues.reduce((acc, cur) => (cur <= 100_000 ? acc + cur : acc), 0);

// part one answer
console.log(sum);

const maxDiskSpace = 70_000_000;
const atLeastSpace = 30_000_000;
const currentUsedSpace = maxDiskSpace - arrayOfValues[0];
const minSpaceToDelete = atLeastSpace - currentUsedSpace;

const filteredValues = sortBy(arrayOfValues.filter((val) => val >= minSpaceToDelete));

// part two answer
console.log(filteredValues.at(0));
