#!/usr/bin/node

const fs = require('fs');
const sys_args = process.argv;

fs.readFile(String(sys_args[2]), 'utf-8', (err, data) => {
    if (err)
        console.log(err)
    else
        console.log(data)
})