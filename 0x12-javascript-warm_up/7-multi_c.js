#!/usr/bin/node
let iter = process.argv[2];
let index = 0;
if (iter === undefined || isNaN(iter)) {
  console.log('Missing number of occurences');
} else {
  for (index = 0; index < parseInt(iter, 10); index++) {
    console.log('C is fun');
  }
}

