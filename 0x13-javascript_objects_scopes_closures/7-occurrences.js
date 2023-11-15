#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let idx = -1;
  let occur = 0;

  while (++idx < list.length) {
    if (list[idx] === searchElement) {
      occur++;
    }
  }

  return (occur);
}
