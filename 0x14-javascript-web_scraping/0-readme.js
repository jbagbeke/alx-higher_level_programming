#!/usr/bin/node

const fs = require('fs');
const sysArgs = process.argv;

fs.readFile(String(sysArgs[2]), 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
