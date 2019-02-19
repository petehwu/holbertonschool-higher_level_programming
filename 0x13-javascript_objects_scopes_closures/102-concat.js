#!/usr/bin/node
// concatenates 2 files into 3rd file
let fileA = process.argv[2];
let fileB = process.argv[3];
let fileC = process.argv[4];
if (fileA === undefined || fileB === undefined || fileC === undefined) {
  console.log('Error: Usage ./102-concat.js <fileA> <fileB> <fileC>');
} else {
  let fs = require('fs');
  let dataA;
  let dataB;
  try {
    dataA = fs.readFileSync(fileA, 'utf8');
  } catch (e) {
    console.log('Error:', e.stack);
  }
  try {
    dataB = fs.readFileSync(fileB, 'utf8');
  } catch (e) {
    console.log('Error:', e.stack);
  }
  try {
    fs.writeFileSync(fileC, dataA + dataB);
  } catch (e) {
    console.log('Error:', e.stack);
  }
}
