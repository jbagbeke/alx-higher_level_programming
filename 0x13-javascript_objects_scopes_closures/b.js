#!/usr/bin/node

const myObject = { key1: 'value1', key2: 'value2', key3: 'value3' };

Object.keys(myObject).forEach(key => {
  const value = myObject[key];
  console.log(`${key}: ${value}`);
});

