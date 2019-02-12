#!/usr/bin/node
let vals = 0;
process.argv.forEach((val, index) => {
  if (index === 2) {
    vals += 1;
    console.log(val);
  }
});
if (vals === 0) {
  console.log('No argument');
}
