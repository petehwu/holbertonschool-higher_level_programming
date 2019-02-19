#!/usr/bin/node
// gets a json and grabs a value

const request = require('request');
const uri = process.argv[2];
if (uri === undefined) {
  console.log('Error: Usage ./6-completed_tasks.js <url>');
} else {
  request.get({ url: uri, json: true }, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let newDict = {};
      let index = 0;
      for (index = 0; index < body.length; index++) {
        if (body[index].completed) {
          if (body[index].userId in newDict) {
            newDict[body[index].userId] += 1;
          } else {
            newDict[body[index].userId] = 1;
          }
        }
      }
      console.log(newDict);
    }
  });
}
