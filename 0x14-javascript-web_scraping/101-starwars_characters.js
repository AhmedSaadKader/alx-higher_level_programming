#!/usr/bin/node

const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) throw err;
  const film = JSON.parse(body);
  const characters = [];

  Promise.all(
    film.characters.map((characterUrl) => new Promise((resolve, reject) => {
      request(characterUrl, (error, res, bod) => {
        if (error) reject(error);
        resolve(JSON.parse(bod));
      });
    }))
  )
    .then((allCharacters) => {
      film.characters.forEach((characterUrl) => {
        const character = allCharacters.find((char) => char.url === characterUrl);
        if (character) {
          characters.push(character.name);
        }
      });
      characters.forEach((name) => console.log(name));
    })
    .catch((error) => {
      throw error;
    });
});
