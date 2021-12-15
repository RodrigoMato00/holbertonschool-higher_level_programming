#!/usr/bin/node
const dict = require('./101-data.js').dict;
const MyDict = {};
for (const key in dict) {
  if (MyDict[dict[key]] === undefined) {
    MyDict[dict[key]] = [key];
  } else {
    MyDict[dict[key]].push(key);
  }
}
console.log(MyDict);
