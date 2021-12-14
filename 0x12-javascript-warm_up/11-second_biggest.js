#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const i = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((j, k) => j - k);
  console.log(i[i.length - 2]);
}
