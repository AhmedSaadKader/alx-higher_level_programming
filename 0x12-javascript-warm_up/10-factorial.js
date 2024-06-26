#!/usr/bin/node
const { argv } = require('node:process');
const num = parseInt(argv[2]);
function factorial (num) {
  if (isNaN(num) || num === 1) return 1;
  if (num < 0) return -1;
  return num * factorial(num - 1);
}
console.log(factorial(num));
