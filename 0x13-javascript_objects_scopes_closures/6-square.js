#!/usr/bin/node
// square class definition 2
const Squareprev = require('./5-square');

module.exports = class Square extends Squareprev {
  charPrint (c) {
    let index = 0;
    if (c === undefined) {
      c = 'X';
    }
    for (index = 0; index < this.height; index++) {
      console.log(c.repeat(this.height));
    }
  }
};
