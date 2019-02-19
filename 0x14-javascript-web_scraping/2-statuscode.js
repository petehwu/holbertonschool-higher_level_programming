#!/usr/bin/node
// gets status code from http request

const request = require('request');
let uri = process.argv[2];
if (uri === undefined) {
  console.log('Error: Uszge ./2-statuscode.js <URL>');
} else {
  request.get(uri).on('response', function(response) {
    console.log('code: ' + response.statusCode);
  });
}
