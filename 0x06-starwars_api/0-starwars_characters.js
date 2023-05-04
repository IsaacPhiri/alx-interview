#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const charactersUrls = JSON.parse(body).characters;

  charactersUrls.forEach(function (url) {
    request(url, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }

      const characterName = JSON.parse(body).name;
      console.log(characterName);
    });
  });
});
