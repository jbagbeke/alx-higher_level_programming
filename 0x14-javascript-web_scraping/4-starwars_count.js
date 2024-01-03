#!/usr/bin/node

const request = require('request');
const sysArgs = process.argv;

request(String(sysArgs[2]), (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const peopleChar = JSON.parse(body).results;
    let wedge = 0;
    const wedgeId = 'https://swapi-api.alx-tools.com/api/people/18/';

    for (let i = 0; i < peopleChar.length; i++) {
      console.log(i);
      if (peopleChar[i].characters.includes(wedgeId)) {
        wedge++;
      }
    }

    console.log(wedge);
  }
});
