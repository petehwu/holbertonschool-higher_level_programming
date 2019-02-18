#!/usr/bin/node
// declare empty Rectangle class
module.exports = class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || isNaN(h) || parseInt(w) < 1 || parseInt(h) < 1) {
    } else {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let index = 0;
    for (index = 0; index < this.height; index++) {
      console.log('X'.repeat(this.width));
    }
  }
};
