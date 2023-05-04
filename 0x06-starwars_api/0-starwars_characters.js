#!/usr/bin/node
//a script that prints all characters of a Star Wars movie

const request = require("request");

// get the movie ID from the command line arguments
const movieId = process.argv[2];

// check if movie ID is missing or not an integer
if (!movieId || isNaN(parseInt(movieId))) {
  console.log("Please enter a valid movie ID");
  return;
}

// make a request to the Star Wars API to get information about the movie
request(
  `https://swapi.dev/api/films/${movieId}/`,
  (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    // parse the response body as JSON
    const movie = JSON.parse(body);

    // get the list of characters from the movie information
    const charactersUrls = movie.characters;

    // print each character's name
    charactersUrls.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }

        // parse the response body as JSON
        const character = JSON.parse(body);

        console.log(character.name);
      });
    });
  }
);
