#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) throw error;
  const userTasksCompleted = {};
  const todos = JSON.parse(body);
  todos.forEach(element => {
    if (element.completed === true) {
      if (element.userId in userTasksCompleted) {
        userTasksCompleted[element.userId] += 1;
      } else {
        userTasksCompleted[element.userId] = 1;
      }
    }
  });
  console.log(userTasksCompleted);
});
