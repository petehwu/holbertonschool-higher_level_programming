#!/usr/bin/node
// gets a json and grabs a value

const request = require('request');
const fs = require('fs');
request.contentType = 'json';
const uri = process.argv[2];
const file = process.argv[3];
if (uri === undefined || file === undefined) {
  console.log('Error: Usage ./5-request_store.js <url> <filename>');
} else {
  request.get({ url: uri, json: true }, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      try {
        fs.writeFileSync(file, body, 'utf8');
      } catch (err) {
        console.log(err);
      }
    }
  });
}
