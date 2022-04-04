#!/usr/bin/node
let i = 0;
const n = parseInt(process.argv[2], 10);
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  while (i < n) {
    console.log('C is fun');
    i++;
  }
}
