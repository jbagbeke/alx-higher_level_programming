#!/usr/bin/node

function factorial (number) {
  let newNum;

  if (number === 0 || number === 1 || !number) {
    return (1);
  }

  newNum = number;
  const factorialNum = factorial(--number);
  newNum = newNum * factorialNum;

  return (newNum);
}

const factNumber = factorial(process.argv[2]);
console.log(factNumber);
