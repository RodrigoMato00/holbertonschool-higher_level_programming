#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((counter, actual) => actual === searchElement ? counter + 1 : counter, 0);
};
