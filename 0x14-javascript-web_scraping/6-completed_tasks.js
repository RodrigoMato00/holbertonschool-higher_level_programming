#!/usr/bin/node

/*
Write a script that computes the number of tasks completed by user id.
-The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
-Only print users with completed task
-You must use the module request
*/

const req = require('request');

req(process.argv[2], function (error, response, body) {
  if (error) console.log(error);

  else {
    const todos = JSON.parse(body);
    const print = {};

    for (const t of todos) {
      if (t.completed) {
        if (!print[t.userId]) print[t.userId] = 1;

        else print[t.userId]++;
      }
    }
    console.log(print);
  }
});
