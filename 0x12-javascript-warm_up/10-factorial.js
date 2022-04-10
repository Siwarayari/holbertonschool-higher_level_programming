#!/usr/bin/node
const n = parseInt(process.argv[2]);
function factorial (n) {
  if (process.argv.length <= 2 || n === 0) {
    return 1;
  }
  return (n * factorial(n - 1));
}
console.log(factorial(n));
