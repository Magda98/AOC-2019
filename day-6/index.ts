/* eslint-disable no-console */
import fs from 'fs';
import {
  chunk, flatten, minBy, uniq,
} from 'lodash-es';

function findMarker(input: string[], data: string, chunkSize = 4) {
  // get the window sliding of input array arrays of chunkSize
  const arrayOfChunks = flatten(input.map((_, index) => chunk(input.slice(index), chunkSize)));
  // filter all unique element arrays
  const uniqueStringArray = arrayOfChunks.filter((marker) => uniq(marker).length === chunkSize);
  const index = minBy(uniqueStringArray, (m) => data.indexOf(m.join('')));
  return index ? data.lastIndexOf(index.join('')) + chunkSize : -1;
}

const filepath = new URL('day6.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');
const input = [...data];

const firstMarkerIndexFirstTask = findMarker(input, data);
// part one answer
console.log(firstMarkerIndexFirstTask);

const firstMarkerIndexSecondTask = findMarker(input, data, 14);
// part two answer
console.log(firstMarkerIndexSecondTask);
