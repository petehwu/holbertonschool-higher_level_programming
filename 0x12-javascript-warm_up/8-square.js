#!/usr/bin/node
let iter = process.argv[2];
let index = 0;
if (iter === undefined || isNaN(iter)) {
  console.log('Missing number of occurences');
} else {
  iter = parseInt(iter, 10);
  for (index = 0; index < iter; index++) {
    console.log('X'.repeat(iter));
  }
}
