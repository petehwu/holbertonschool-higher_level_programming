#!/usr/bin/node
// converts to another base
exports.converter = function (base) {
  return function (val) {
    return (val.toString(base));
  };
};
