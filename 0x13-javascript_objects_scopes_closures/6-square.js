#!/usr/bin/node

const Square = require('./5-square.js');

class SquareTwo extends Square {
  charPrint (c) {
    if (c) {
      let idx = 0;
      while (idx < this.height) {
        console.log('c'.repeat(this.width));
        idx++;
      }
    } else {
      this.print();
    }
  }
}

module.exports = SquareTwo;
