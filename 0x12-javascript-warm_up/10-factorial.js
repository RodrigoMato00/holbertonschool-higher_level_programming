#!/usr/bin/node
function factorial (num) {
  num = Number(num);
  if (isNaN(num * (num - 1))) {
    return (1);
  } else if (num === 0) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}

console.log(factorial(process.argv[2]));
