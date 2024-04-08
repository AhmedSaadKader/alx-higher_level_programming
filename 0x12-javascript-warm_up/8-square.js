#!/usr/bin/node
const { argv } = require('node:process');
const number = parseInt(argv[2]);
if (!number) console.log('Missing size');
else {
  for (let i = 0; i < number; i++) {
    row = '';
    for (let l = 0; l < number; l++) {
      row += 'X';
    }
    console.log(row);
  }
}
