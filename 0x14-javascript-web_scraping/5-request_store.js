#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const sysArgs = process.argv;

request.get(sysArgs[2], (err, response, body) => {
    if (err) {
        console.log(err);
    }
    else {
        fs.writeFile(sysArgs[3], body.toString('utf-8'), (err) => {
            if (err) {
                console.log(err)
            }
        });
    }
});