#!/usr/bin/node

// Retrieve and display character names from the Star Wars API
// for a specific film ID.
const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  for (const characterURL of characters) {
    req.get(characterURL, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const characterData = JSON.parse(body1);
      console.log(characterData.name);
    });
  }
});
