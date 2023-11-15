#!/usr/bin/node

let idx = 0;
const { list } = require('./100-data.js');

console.log(list);
console.log(list.map(arg => arg * idx++));
