#!/usr/bin/node
// imports a list and uses it to make new list

const list = require('./100-data').list;
const newlist = list.map(function (x, index) { return (x * index); });
console.log(list);
console.log(newlist);
