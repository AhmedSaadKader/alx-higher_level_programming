#!/usr/bin/node

const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) throw err;
  const film = JSON.parse(body);
  film.characters.forEach((characterUrl) => {
    request(characterUrl, (error, res, bod) => {
      if (error) throw error;
      const character = JSON.parse(bod);
      console.log(character.name);
    });
  });
});
