#!/usr/bin/node
const { argv } = require('node:process');
const num = parseInt(argv[2]);
const factorial = (num) => {
  if (isNaN(num)) return 1;
  if (num === 1) return 1;
  return num * factorial(num - 1);
};
console.log(factorial(num));
