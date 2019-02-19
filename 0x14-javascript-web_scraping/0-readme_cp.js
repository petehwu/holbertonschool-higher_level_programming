#!/usr/bin/node
// reads and prints content of a file
let file = process.argv[2];
if (file === undefined) {
  console.log('Error: Usage ./0-readme.js <file_to_read>');
} else {
  let fs = require('fs');
  fs.readFile(file, 'utf8', function(err, data) {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}
