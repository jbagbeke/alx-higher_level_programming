#!/usr/bin/node

const sysArgs = process.argv;
const request = require('request');

request(sysArgs[2], (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ', res.statusCode);
  }
});
