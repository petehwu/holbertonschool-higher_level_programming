#!/usr/bin/node
// reverses a list without using builtin
exports.esrever = function (list) {
  let low = 0;
  let high = list.length - 1;
  let temp;
  for (low = 0; low < high; low++, high--) {
    temp = list[high];
    list[high] = list[low];
    list[low] = temp;
  }
  return (list);
};
