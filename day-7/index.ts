/* eslint-disable no-plusplus */
import fs from 'fs';
import { uniqBy } from 'lodash-es';

const filepath = new URL('day7.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');

const numbers = data.split('\n').map((value) => {
  const [rawResult, rest] = value.split(':');
  const result = Number(rawResult);
  const nums = rest.split(' ').map(Number);

  return [result, nums.slice(1)];
});

function combRep(arr: number[], length: number): number[][] {
  const len = length ?? arr.length;
  const d = Array(len);
  const results = [];
  (function f(position, start) {
    if (position === len) {
      results.push(d.slice());
      return;
    }
    for (let i = start; i < arr.length; ++i) {
      d[position] = arr[i];
      f(position + 1, i);
    }
  }(0, 0));
  return results;
}

console.log(combRep([1, 2], 1));
let validLinesSum = 0;
for (const [result, nums] of numbers) {
  const len = (nums as Array<number>).length - 1;
  const combinations = uniqBy(combRep([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], len), (value) => Number(value.join('')));

  for (const combination of combinations) {
    let res = 0;

    for (const [index, num] of (nums as number[]).entries()) {
      if (index === 0) {
        res += num;
      } else if (index > 0 && combination[index - 1] === 1) {
        res += num;
      } else if (index > 0 && combination[index - 1] === 2) {
        res *= num;
      }
    }
    if (res === result) {
      validLinesSum += result;
      break;
    }
  }
}

console.log(validLinesSum);
