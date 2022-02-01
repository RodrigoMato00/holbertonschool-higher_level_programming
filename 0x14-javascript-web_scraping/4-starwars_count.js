#!/usr/bin/node

/*
Write a script that prints the number of movies where the character “Wedge Antilles” is present.
-The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
-Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
-You must use the module request
*/

const req = require('request');
const id = '/18/';
const url = process.argv[2];

req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }

  let instance = 0;

  for (const film of JSON.parse(body).results) {
    for (const char of film.characters) {
      if (char.includes(id)) {
        instance += 1;
      }
    }
  }
  console.log(instance);
});
