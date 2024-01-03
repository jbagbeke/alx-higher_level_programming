#!/usr/bin/node

const request = require('request');
const sysArgs = process.argv;
const dictionary = {};

let userId;

request(sysArgs[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    JSON.parse(body).forEach((user) => {
      userId = user.userId;

      if (user.completed === true) {
        if (!dictionary[String(userId)]) {
          dictionary[String(userId)] = 1;
        } else {
          dictionary[String(userId)] = dictionary[String(userId)] + 1;
        }
      }
    });

    console.log(dictionary);
  }
});
