#!/usr/bin/node

exports.esrever = function (list) {
  let idx = list.length;
  let idx2 = 0;
  const newList = [];

  while (--idx >= 0) {
    newList[idx2++] = list[idx];
  }

  return (newList);
};
