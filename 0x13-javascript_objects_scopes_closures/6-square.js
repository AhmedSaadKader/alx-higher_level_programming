#!/usr/bin/node
const SquareParent = require('./5-square');
class Square extends SquareParent {
  charPrint (c = 'X') {
    let side = '';
    for (let i = 0; i < this.width; i++) {
      side += c;
    }
    for (let l = 0; l < this.height; l++) {
      console.log(side);
    }
  }
}

module.exports = Square;
