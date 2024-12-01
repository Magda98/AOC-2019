/* eslint-disable no-console */
import fs from 'fs';
import { sumBy, zip } from 'lodash-es';

const filepath = new URL('day1.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');
const dataArray = data.split('\n');

const leftData = dataArray.map((line) => Number(line.split('   ')[0]));
const rightData = dataArray.map((line) => Number(line.split('   ')[1]));
const sortedLeftData = leftData
  .map((value) => value)
  .sort((value, nextValue) => value - nextValue);
const sortedRightData = rightData
  .map((value) => value)
  .sort((value, nextValue) => value - nextValue);

// part 1
const zippedData = zip(sortedLeftData, sortedRightData);
const sumOfDistances = sumBy(zippedData, ([left, right]) => Math.abs((left ?? 0) - (right ?? 0)));
console.log(sumOfDistances);

// part 2
const rightDataMap = new Map<number, number>();
sortedRightData.forEach((value) => {
  const mapValue = rightDataMap.get(value);
  return rightDataMap.set(value, (mapValue ?? 0) + 1);
});

const similarityScore = sumBy(
  sortedLeftData,
  (value) => (rightDataMap.get(value) ?? 0) * value,
);

console.log(similarityScore);
