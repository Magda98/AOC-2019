/* eslint-disable no-console */
import fs from 'fs';
import {
  flatten,
  maxBy, orderBy, slice, sum,
} from 'lodash-es';

const filepath = new URL('day1.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');

const elvesArray = data.split('\n\n');
const elvesArrayMapped = elvesArray.map((calories) => calories.split('\n').map(Number));
const maxCalories = maxBy(elvesArrayMapped, sum);

// part one answer
console.log(sum(maxCalories));

const orderedCalories = orderBy(elvesArrayMapped, sum, ['desc']);
const topThreeElves = slice(orderedCalories, 0, 3);

// part two answer
console.log(sum(flatten(topThreeElves)));
