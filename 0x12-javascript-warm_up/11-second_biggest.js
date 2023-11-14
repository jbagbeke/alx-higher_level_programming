#!/usr/bin/node

let newCommands = process.argv.slice(2);
let parsedArray;
let firstMax;
let index = 0;
let newArray = [];

parsedArray = newCommands.map(arg => parseInt(arg));
firstMax = Math.max.apply(null, parsedArray);

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
