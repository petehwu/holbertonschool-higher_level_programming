#!/usr/bin/node
// keeps tracks of how many times function called

let cnt = 0;
exports.logMe = function (item) {
  console.log(cnt + ': ' + item);
  cnt++;
};
