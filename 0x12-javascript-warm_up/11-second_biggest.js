#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv.length < 2) console.log(0);
else console.log(argv.sort((a, b) => b - a)[1]);
