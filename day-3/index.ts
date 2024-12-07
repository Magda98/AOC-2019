import fs from 'fs';
import { sumBy } from 'lodash-es';

const filepath = new URL('day3.txt', import.meta.url);
const data = await fs.promises.readFile(filepath, 'utf8');

function multiplyAndSum(
  inputString: string,
  regexExp: RegExp,
  sumCallback: (mul: RegExpExecArray) => number,
) {
  const multiplications = [...inputString.matchAll(regexExp)];
  return sumBy(multiplications, (mul) => sumCallback(mul));
}

// part 1
console.log(
  multiplyAndSum(data, /mul\([-0-9]+,[-0-9]+\)/g, (mul) => {
    const [numberOne, numberTwo] = [...mul[0].matchAll(/[-0-9]+/g)];
    return Number(numberOne[0]) * Number(numberTwo[0]);
  }),
);

// part 2
const sumPartTwo = () => {
  let doFlag = true;
  return (mul: RegExpExecArray) => {
    if (mul[0] === 'do()') {
      doFlag = true;
      return 0;
    }
    if (mul[0] === "don't()") {
      doFlag = false;
      return 0;
    }

    const [numberOne, numberTwo] = [...mul[0].matchAll(/[-0-9]+/g)];
    return doFlag ? Number(numberOne[0]) * Number(numberTwo[0]) : 0;
  };
};

console.log(
  multiplyAndSum(
    data,
    /mul\([-0-9]+,[-0-9]+\)|do\(\)|don't\(\)/g,
    sumPartTwo(),
  ),
);
