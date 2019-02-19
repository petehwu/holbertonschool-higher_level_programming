#!/usr/bin/node
// reads and prints content of a file
let file = process.argv[2];
let fs = require('fs');
if (file === undefined) {
  console.log('Error: Usage ./0-readme.js <file_to_read>');
} else {
  fs.readFile(file, 'utf-8', function (err, data) {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}
