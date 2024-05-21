#!/usr/bin/node

const request = require('request');
const url = `${process.argv[2]}`;
request(url, (error, response, body) => {
  if (error) throw error;
  const results = JSON.parse(body).results;
  let count = 0;
  results.forEach((result) => {
    result.characters.forEach((character) => {
      if (character.endsWith('/18/')) count++;
    });
  });
  console.log(count);
});
