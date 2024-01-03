#!/usr/bin/node

const fs = require('fs');
const sysArgs = process.argv;

fs.writeFile(String(sysArgs[2]), String(sysArgs[3]), (err) => {
  if (err) {
    console.log(err);
  }
});
