/* eslint-disable operator-linebreak */
/* eslint-disable no-restricted-syntax */
/* eslint-disable no-console */
import fs from 'fs';

const filepath = new URL('day4.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');
const dataArray = data.split('\n').map((line) => line.split(''));

// part 1
let xmasCount = 0;
for (const [index, line] of dataArray.entries()) {
  for (const [innerIndex, character] of line.entries()) {
    if (
      character === 'X' &&
      dataArray?.[index]?.[innerIndex + 1] === 'M' &&
      dataArray?.[index]?.[innerIndex + 2] === 'A' &&
      dataArray?.[index]?.[innerIndex + 3] === 'S'
    ) {
      xmasCount += 1;
    }

    if (
      character === 'X' &&
      dataArray?.[index + 1]?.[innerIndex] === 'M' &&
      dataArray?.[index + 2]?.[innerIndex] === 'A' &&
      dataArray?.[index + 3]?.[innerIndex] === 'S'
    ) {
      xmasCount += 1;
    }

    if (
      character === 'X' &&
      dataArray?.[index - 1]?.[innerIndex] === 'M' &&
      dataArray?.[index - 2]?.[innerIndex] === 'A' &&
      dataArray?.[index - 3]?.[innerIndex] === 'S'
    ) {
      xmasCount += 1;
    }

    if (
      character === 'X' &&
      dataArray?.[index]?.[innerIndex - 1] === 'M' &&
      dataArray?.[index]?.[innerIndex - 2] === 'A' &&
      dataArray?.[index]?.[innerIndex - 3] === 'S'
    ) {
      xmasCount += 1;
    }

    if (
      character === 'X' &&
      dataArray?.[index + 1]?.[innerIndex + 1] === 'M' &&
      dataArray?.[index + 2]?.[innerIndex + 2] === 'A' &&
      dataArray?.[index + 3]?.[innerIndex + 3] === 'S'
    ) {
      xmasCount += 1;
    }
    if (
      character === 'X' &&
      dataArray?.[index + 1]?.[innerIndex - 1] === 'M' &&
      dataArray?.[index + 2]?.[innerIndex - 2] === 'A' &&
      dataArray?.[index + 3]?.[innerIndex - 3] === 'S'
    ) {
      xmasCount += 1;
    }
    if (
      character === 'X' &&
      dataArray?.[index - 1]?.[innerIndex + 1] === 'M' &&
      dataArray?.[index - 2]?.[innerIndex + 2] === 'A' &&
      dataArray?.[index - 3]?.[innerIndex + 3] === 'S'
    ) {
      xmasCount += 1;
    }
    if (
      character === 'X' &&
      dataArray?.[index - 1]?.[innerIndex - 1] === 'M' &&
      dataArray?.[index - 2]?.[innerIndex - 2] === 'A' &&
      dataArray?.[index - 3]?.[innerIndex - 3] === 'S'
    ) {
      xmasCount += 1;
    }
  }
}

console.log(xmasCount);

// part 2
let maxCount = 0;
for (const [index, line] of dataArray.entries()) {
  for (const [innerIndex, character] of line.entries()) {
    if (
      character === 'M' &&
      dataArray?.[index + 1]?.[innerIndex + 1] === 'A' &&
      dataArray?.[index + 2]?.[innerIndex + 2] === 'S' &&
      dataArray?.[index + 2]?.[innerIndex] === 'M' &&
      dataArray?.[index]?.[innerIndex + 2] === 'S'
    ) {
      maxCount += 1;
    }

    if (
      character === 'M' &&
      dataArray?.[index - 1]?.[innerIndex + 1] === 'A' &&
      dataArray?.[index - 2]?.[innerIndex + 2] === 'S' &&
      dataArray?.[index]?.[innerIndex + 2] === 'M' &&
      dataArray?.[index - 2]?.[innerIndex] === 'S'
    ) {
      maxCount += 1;
    }

    if (
      character === 'M' &&
      dataArray?.[index - 1]?.[innerIndex - 1] === 'A' &&
      dataArray?.[index - 2]?.[innerIndex - 2] === 'S' &&
      dataArray?.[index - 2]?.[innerIndex] === 'M' &&
      dataArray?.[index]?.[innerIndex - 2] === 'S'
    ) {
      maxCount += 1;
    }

    if (
      character === 'M' &&
      dataArray?.[index + 1]?.[innerIndex + 1] === 'A' &&
      dataArray?.[index + 2]?.[innerIndex + 2] === 'S' &&
      dataArray?.[index]?.[innerIndex + 2] === 'M' &&
      dataArray?.[index + 2]?.[innerIndex] === 'S'
    ) {
      maxCount += 1;
    }
  }
}

console.log(maxCount);
