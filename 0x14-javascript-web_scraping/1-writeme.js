#!/usr/bin/node

/*
Write a script that prints all characters of a Star Wars movie:
-The first argument is the Movie ID - example: 3 = “Return of the Jedi”
-Display one character name by line in the same order of the list “characters” in the /films/ response
-You must use the Star wars API
-You must use the module request
*/
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (error) {
  if (error) console.log(error);
});
