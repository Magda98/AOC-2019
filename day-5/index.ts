/* eslint-disable no-console */
import fs from 'fs';
import { chunk } from 'lodash-es';

const filepath = new URL('day5.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');

const [stackStrings, input] = data.split('\n\n').map((arr) => arr.split('\n'));

const stack = stackStrings.map((row) => {
  const chunks = chunk(Array.from(row), 4);
  return chunks.map((c) => c.at(1));
}).slice(0, -1);

const cargoCrane = stack[0].map((_, colIndex) => (
  [...stack.map((row) => row[colIndex]).filter((cell) => cell !== ' ')].reverse()
));

function moveCargo(count: number, from: number, to: number) {
  // part one
  // const cargoToMove = cargoCrane.at(from - 1)!.splice(-count, count).reverse();

  // part two - without reverse, because
  //  cargoCrane has the ability to pick up and move multiple crates at once
  const cargoToMove = cargoCrane.at(from - 1)!.splice(-count, count);
  cargoCrane[to - 1] = [...cargoCrane[to - 1], ...cargoToMove];
}

input.forEach((line) => {
  const [, count, , from, , to] = line.split(' ').map(Number);
  moveCargo(count, from, to);
});

// answer
console.log(cargoCrane.map((s) => s.pop()).join(''));
