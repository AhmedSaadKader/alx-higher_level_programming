#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    let side = '';
    for (let i = 0; i < this.width; i++) {
      side += 'X';
    }
    for (let l = 0; l < this.height; l++) {
      console.log(side);
    }
  }
}

module.exports = Rectangle;
