#!/usr/bin/node
let val = process.argv[2];
function factorial (val) {
  if (val === 1 || isNaN(val)) {
    return 1;
  } else {
    return val * factorial(val - 1);
  }
}
console.log(factorial(val));
