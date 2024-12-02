/* eslint-disable no-restricted-syntax */
/* eslint-disable no-console */
import fs from 'fs';
import { sumBy } from 'lodash-es';

const filepath = new URL('day2.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');
const dataArray = data.split('\n');
const parsedReports = dataArray.map((report) => report.split(' ').map(Number));

function isSafe(levels: number[]) {
  const checkSum = levels.every(
    (value, index) => index === 0 || Math.abs(value - levels[index - 1]) <= 3,
  );
  const isIncreasing = levels.every(
    (value, index) => index === 0 || value > levels[index - 1],
  );
  const isDecreasing = levels.every(
    (value, index) => index === 0 || value < levels[index - 1],
  );

  return checkSum && (isDecreasing || isIncreasing);
}

// part 1
const safeReportsCount = sumBy(parsedReports, (report) => (isSafe(report) ? 1 : 0));

console.log(safeReportsCount);

// part 2
const safeReportsCountWithDampener = sumBy(parsedReports, (report) => {
  const isReportSafe = isSafe(report);

  if (isReportSafe) return 1;

  // check other combinations with dumping each report level
  for (const [index] of report.entries()) {
    const removed = [...report.slice(0, index), ...report.slice(index + 1)];
    if (isSafe(removed)) {
      return 1;
    }
  }

  return 0;
});

console.log(safeReportsCountWithDampener);
