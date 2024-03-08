#!/usr/bin/node
const Square_parent = require('./5-square');

class Square extends Square_parent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let res = '';
      for (let j = 0; j < this.width; j++) {
        res += c;
      }
      console.log(res);
    }
  }
}

module.exports = Square;
