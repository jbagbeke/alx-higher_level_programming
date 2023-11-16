#!/usr/bin/node

const { dict } = require('./101-data.js');

const newDict = Object.entries(dict).reduce((acc, [key, value]) => {
  acc[String(value)] = acc[String(value)] || [];

  acc[String(value)].push(key);

  return (acc);
}, {});

console.log(newDict);
