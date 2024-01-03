#!/usr/bin/node

const sysArgs = process.argv;
const request = require('request');

request.get(sysArgs[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ', response.statusCode);
  }
});
