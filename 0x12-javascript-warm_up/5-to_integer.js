#!/usr/bin/node
let n = Number.isNaN(parseInt(process.argv[2], 10));
if (n) {
  console.log('Not a number');
} else {
  n = parseInt(process.argv[2], 10);
  console.log('My number: ' + n);
}
