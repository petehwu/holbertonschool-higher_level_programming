#!/usr/bin/node
// imports a list and uses it to make new list

const list = require('./100-data').list;
let len = list.length;
let index = 0;
let newlist = [];
for (index = 0; index < len; index++) {
  newlist.push(parseInt(list[index]) * index);
}
console.log(list);
console.log(newlist);
