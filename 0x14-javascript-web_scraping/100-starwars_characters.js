#!/usr/bin/node

const request = require('request');
const sysArgs = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/{id}/';

request(url.replace('{id}', sysArgs[2]), (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;

    characters.forEach((user) => {
      request(user, (error, res, userData) => {
        if (err) {
          console.log(error);
        } else {
          console.log(JSON.parse(userData).name);
        }
      });
    });
  }
});
