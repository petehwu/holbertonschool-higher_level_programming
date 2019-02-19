#!/usr/bin/node
// creates a dictionary

const og = require('./101-data').dict;
let newdict = {};
for (let key in og) {
  let val = og[key];
  if (val in newdict) {
    newdict[val].push(key);
  } else {
    newdict[val] = [key];
  }
}
console.log(newdict);
