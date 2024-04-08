#!/usr/bin/node
const process = require('node:process');
process.argv[3]
  ? console.log('Arguments found')
  : process.argv[2]
    ? console.log('Argument found')
    : console.log('No argument');
