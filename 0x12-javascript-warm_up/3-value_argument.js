#!/usr/bin/node
let ar = process.argv[2];
if (ar === undefined) {
  console.log('No argument');
} else {
  console.log(ar);
}
