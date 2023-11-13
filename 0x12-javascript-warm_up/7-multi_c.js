#!/usr/bin/node

const convertedNum = parseInt(process.argv[2]);
let index = 0;

if (convertedNum) {
  while (index < convertedNum) {
    console.log('C is fun');
    index++;
  }
} else {
  console.log('Missing number of occurrences');
}
