#!/usr/bin/node
/*
Write a script that prints all characters of a Star Wars movie:
-The first argument is the Movie ID - example: 3 = “Return of the Jedi”
-Display one character name by line
-You must use the Star wars API
-You must use the module request
*/

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req(url, function (error, response, body) {
  if (error) console.log(error);
  else {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      req(character, function (error, response, body) {
        if (error) console.log(error);
        else console.log(JSON.parse(body).name);
      });
    });
  }
});
