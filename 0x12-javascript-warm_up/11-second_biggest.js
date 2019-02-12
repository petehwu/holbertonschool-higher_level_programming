#!/usr/bin/node
let numList = process.argv.slice(2);
if (numList.length < 2) {
  console.log(0);
} else {
  numList.sort((a, b) => a - b);
  console.log(numList[numList.length - 2]);
}
