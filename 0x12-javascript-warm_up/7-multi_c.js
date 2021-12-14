#!/usr/bin/node
const mul = Math.floor(Number(process.argv[2]));
if (isNaN(mul)) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < mul; count++) {
    console.log('C is fun');
  }
}
