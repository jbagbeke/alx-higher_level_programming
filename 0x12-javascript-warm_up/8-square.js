#!/usr/bin/node

const convertedNum = parseInt(process.argv[2]);
let index = 0;

if (convertedNum) {
  while (index++ < convertedNum) {
    console.log('X'.repeat(convertedNum));
  }
} else {
  console.log('Missing size');
}
