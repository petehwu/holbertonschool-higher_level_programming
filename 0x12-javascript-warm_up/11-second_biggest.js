#!/usr/bin/node
let numList = [];
process.argv.forEach((val, index) => {
  if (index > 1) {
    numList.push(parseInt(val, 10));
  }
});
if (numList.length < 2) {
  console.log(0);
} else {
  numList.sort((a, b) => a - b);
  console.log(numList[numList.length - 2]);
}
