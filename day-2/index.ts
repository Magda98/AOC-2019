/* eslint-disable no-console */
import fs from 'fs';
import { countBy } from 'lodash-es';

const filepath = new URL('day2.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');

const input = data.split('\n');
const movesObject = countBy(input);

let totalScore = 0;
Object.entries(movesObject).forEach(([key, value]) => {
  switch (key) {
    case 'A X':
      totalScore += (1 + 3) * value;
      break;
    case 'A Y':
      totalScore += (2 + 6) * value;
      break;
    case 'A Z':
      totalScore += 3 * value;
      break;
    case 'B X':
      totalScore += value;
      break;
    case 'B Y':
      totalScore += (2 + 3) * value;
      break;
    case 'B Z':
      totalScore += (3 + 6) * value;
      break;
    case 'C X':
      totalScore += (1 + 6) * value;
      break;
    case 'C Y':
      totalScore += 2 * value;
      break;
    case 'C Z':
      totalScore += (3 + 3) * value;
      break;
    default:
      break;
  }
});
// part one answer
console.log(totalScore);

let totalScorePartTwo = 0;
Object.entries(movesObject).forEach(([key, value]) => {
  switch (key) {
    case 'A X':
      totalScorePartTwo += 3 * value;
      break;
    case 'A Y':
      totalScorePartTwo += (1 + 3) * value;
      break;
    case 'A Z':
      totalScorePartTwo += (2 + 6) * value;
      break;
    case 'B X':
      totalScorePartTwo += value;
      break;
    case 'B Y':
      totalScorePartTwo += (2 + 3) * value;
      break;
    case 'B Z':
      totalScorePartTwo += (3 + 6) * value;
      break;
    case 'C X':
      totalScorePartTwo += 2 * value;
      break;
    case 'C Y':
      totalScorePartTwo += (3 + 3) * value;
      break;
    case 'C Z':
      totalScorePartTwo += (1 + 6) * value;
      break;
    default:
      break;
  }
});

// part two answer
console.log(totalScorePartTwo);
