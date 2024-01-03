#!/usr/bin/node

const request = require('request');
const sysArgs = process.argv;

request(String(sysArgs[2]), (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const peopleChar = JSON.parse(body).results;
    let wedge = 0;
    const wedgeId = '18';

    peopleChar.forEach((fdict) => {
      fdict.characters.forEach((char) => {
        if (char.includes(wedgeId)) {
          wedge++;
        }
      });
    });

    console.log(wedge);
  }
});
