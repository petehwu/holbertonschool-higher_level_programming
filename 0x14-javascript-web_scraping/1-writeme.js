#!/usr/bin/node
// writes a string to file
let fs = require('fs');
let file = process.argv[2];
let txt = process.argv[3];
if (file === undefined || txt === undefined) {
  console.log('Error: Usage ./1-writeme.js <file_name> <text_to_write');
} else {
  try {
    fs.writeFileSync(file, txt, 'utf8');
  } catch (err) {
    console.log(err);
  }
}
