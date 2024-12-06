/* eslint-disable max-len */
/* eslint-disable implicit-arrow-linebreak */
/* eslint-disable no-confusing-arrow */
/* eslint-disable no-restricted-syntax */
/* eslint-disable operator-linebreak */
/* eslint-disable no-console */
import fs from 'fs';
import { sumBy } from 'lodash-es';

const filepath = new URL('day5.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');
const [rawPagesOrder, rawPages] = data.split('\n\n');
const orderingRules = rawPagesOrder.split('\n').map((value) => {
  const [firstPage, secondPage] = value.split('|');
  return [Number(firstPage), Number(secondPage)];
});
const manualPages = rawPages
  .split('\n')
  .map((value) => value.split(',').map(Number));
let validManualPages = manualPages.map((value) => value);

for (const orderRule of orderingRules) {
  const [firstPage, secondPage] = orderRule;
  for (const [index, updates] of manualPages.entries()) {
    const firstIndex = updates.findIndex((value) => value === firstPage);
    const secondIndex = updates.findIndex((value) => value === secondPage);
    if (firstIndex > -1 && secondIndex > -1 && secondIndex < firstIndex) {
      validManualPages = validManualPages.map((value, innerIndex) =>
        innerIndex !== index ? value : []);
    }
  }
}

const sumOfMiddlePageNumbers = sumBy(validManualPages, (page) => {
  if (page.length === 0) return 0;
  return page[(page.length - 1) / 2];
});

console.log(sumOfMiddlePageNumbers);
