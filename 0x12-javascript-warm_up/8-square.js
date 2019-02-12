#!/usr/bin/node
let iter = process.argv[2];
let index = 0;
if (iter === undefined || isNaN(iter)) {
  console.log('Missing size');
} else {
  iter = parseInt(iter, 10);
  for (index = 0; index < iter; index++) {
    console.log('X'.repeat(iter));
  }
}
