#!/usr/bin/node
const { argv } = require('node:process');
const number = parseInt(argv[2]);
if (!number) console.log('Missing number of occurrences');
else {
  for (let index = 0; index < number; index++) {
    console.log('C is fun');
  }
}
