#!/usr/bin/node

const convertedNum = parseInt(process.argv[2]);

if (convertedNum) {
  console.log('My number: ' + convertedNum);
} else {
  console.log('Not a number');
}
