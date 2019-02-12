#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let index = 0;
  for (index = 0; index < x; index++) {
    theFunction();
  }
};
