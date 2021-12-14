#!/usr/bin/node
const number = process.argv[2];
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let count = 0; count < parseInt(number); count++) {
    console.log('X'.repeat(parseInt(number)));
  }
}
