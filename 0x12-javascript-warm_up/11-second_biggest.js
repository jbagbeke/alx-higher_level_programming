#!/usr/bin/node

const newCommands = process.argv.slice(2);
let index = 0;
let newArray = [];

const parsedArray = newCommands.map(arg => parseInt(arg));
const firstMax = Math.max.apply(null, parsedArray);

if (parsedArray.length < 2) {
  console.log(0);
} else {
  while (index < parsedArray.length) {
    if (parsedArray[index] !== firstMax) {
      newArray[index] = parsedArray[index];
    }

    index++;
  }

  newArray = newArray.filter(num => num !== undefined && num !== null);
  console.log(Math.max.apply(null, newArray));
}
