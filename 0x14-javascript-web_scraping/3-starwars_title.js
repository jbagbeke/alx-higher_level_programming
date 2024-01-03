#!/usr/bin/node

const request = require('request');
const sysArgv = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/{id}';

request(url.replace('{id}', sysArgv[2]), (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
