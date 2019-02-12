#!/usr/bin/node
let arg1 = process.argv[2];
if (arg1 === undefined || isNaN(arg1)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(arg1, 10));
}
