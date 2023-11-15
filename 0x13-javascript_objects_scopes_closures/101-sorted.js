#!/usr/bin/node

const { dict } = require('./101-data.js');

const newDict = {};
const dictKey = [];
const dictValue = [];


Object.entries(dict).forEach(([key, value]) => {
  if (!dictKey.includes(value)) {
    dictKey.push(value);
  }

  dictValue.push(key);
});

let idx = 0;

while (idx < dictKey.length) {
  const firstKey = dictKey[idx];
  let index = 0;
  const currentList = [];

  while (index < dictValue.length) {

    if (dict[dictValue[index]] === firstKey) {
      currentList.push(dictValue[index]);
    }

    index++;
  }

  newDict[String(dictKey[idx])] = currentList;
  idx++;
}

console.log(newDict);
