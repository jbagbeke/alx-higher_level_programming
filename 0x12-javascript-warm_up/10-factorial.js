#!/usr/bin/node

function factorial (number) {
  let factorialNum;
  let newNum;
  let abcd;

  if (number === 0 || number === 1 || !number) {
    return (1);
  }

  newNum = number;
  factorialNum = factorial(--number);
  newNum = newNum * factorialNum;

  return (newNum);
}

const factNumber = factorial(parseInt(process.argv[2]));
console.log(factNumber);
