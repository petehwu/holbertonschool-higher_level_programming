#!/usr/bin/node
// counts number of occurences of value in list
exports.nbOccurences = function (list, searchElement) {
  let len = list.length;
  let index = 0;
  let occur = 0;
  for (index = 0; index < len; index++) {
    if (searchElement === list[index]) {
      occur += 1;
    }
  }
  return (occur);
};
