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
  const comb = Array(len);
  const results = [];
  (function f(position, start) {
    if (position === len) {
      results.push(comb.slice());
      return;
    }
    for (let i = start; i < arr.length; ++i) {
      comb[position] = arr[i];
      f(position + 1, i);
    }
  }(0, 0));
  return results;
}

const twoSignsCombinations: number[][][] = [];
for (let i = 1; i < 13; i++) {
  const combination = uniqBy(combRep([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2], i), (value) => Number(value.join('')));
  twoSignsCombinations.push(combination);
}

let invalidLines: (number | number[])[][] = [];
let validLinesSum = 0;
for (const [result, nums] of numbers) {
  const len = (nums as Array<number>).length - 1;
  const combinations = twoSignsCombinations[len];

  let isValid = false;
  for (const combination of combinations) {
    let res = 0;
    for (const [index, num] of (nums as number[]).entries()) {
      if (index === 0) {
        res += num;
      } else if (index > 0 && combination[index - 1] === 1) {
        res += num;
      } else if (index > 0 && combination[index - 1] === 2) {
        res *= num;
      } else if (index > 0 && combination[index - 1] === 3) {
        res = Number(`${res}${num}`);
      }
    }
    if (res === result) {
      validLinesSum += result;
      isValid = true;
      break;
    }
  }
  if (!isValid) {
    invalidLines = [...invalidLines, [result, nums]];
  }
}

console.log(validLinesSum);

const threeSignsCombinations: number[][][] = [];
for (let i = 1; i < 13; i++) {
  const combination = uniqBy(combRep([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], i), (value) => Number(value.join('')));
  threeSignsCombinations.push(combination);
}

let partTwoSum = validLinesSum;

for (const [result, nums] of invalidLines) {
  const len = (nums as Array<number>).length - 1;
  const combinationss = threeSignsCombinations[len];
  for (const combination of combinationss) {
    let res = 0;

    for (const [index, num] of (nums as number[]).entries()) {
      if (index === 0) {
        res += num;
      } else if (index > 0 && combination[index - 1] === 1) {
        res += num;
      } else if (index > 0 && combination[index - 1] === 2) {
        res *= num;
      } else if (index > 0 && combination[index - 1] === 3) {
        res = Number(`${res}${num}`);
      }
    }
    if (res === result) {
      partTwoSum += result;
      break;
    }
  }
}

console.log(partTwoSum);
