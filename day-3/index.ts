/* eslint-disable no-console */
import fs from 'fs';
import { chunk, countBy, intersection, upperCase } from 'lodash-es';


const filepath = new URL('day3.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');

const input = data.split('\n');

function split(str, index) {
  const result = [str.slice(0, index), str.slice(index)];

  return result;
}

function getCharaterValue(character: string): number {
  const asciiCode = character.charCodeAt(0);

  if (character === upperCase(character)) return (asciiCode - 38)

  return (asciiCode - 96)
}

let score = 0;
input.forEach((line) => {
  const [first, second] = split(line, line.length / 2);
  const firstArray = [...first];
  const secondArray = [...second];

  const [character] = intersection(firstArray, secondArray);
  score += getCharaterValue(character);

})

// part one answer
console.log(score);

const chunkedInput = chunk(input, 3);

let scorePartTwo = 0;
chunkedInput.forEach((lines) => {
  const [first, second, third] = lines
  const firstArray = [...first];
  const secondArray = [...second];
  const thirdArray = [...third];

  const [character] = intersection(firstArray, secondArray, thirdArray);
  scorePartTwo += getCharaterValue(character);

})

// part two answer
console.log(scorePartTwo);