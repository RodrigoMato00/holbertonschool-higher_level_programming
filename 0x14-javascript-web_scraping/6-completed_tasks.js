#!/usr/bin/node
/*
Write a script that computes the number of tasks completed by user id.
-The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
-Only print users with completed task
-You must use the module request
*/
const req = require('request');
const url = process.argv[2];

req(url, function (error, response, body) {
  if (error) console.log(error);

  else if (response.statusCode === 200) {
    const completed = {};

    JSON.parse(body).forEach(task => {
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    });
    console.log(completed);
  }
});
