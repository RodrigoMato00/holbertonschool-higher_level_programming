#!/usr/bin/node
const ImpDict = require('./101-data.js').ImpDict;
let MyDict = {};
for (const value in ImpDict) {
  if (MyDict[ImpDict[value]] === undefined) {
    MyDict[ImpDict[value]] = [value];
  } else {
    MyDict[ImpDict[value]].push(value);
  }
}
console.log(MyDict);
