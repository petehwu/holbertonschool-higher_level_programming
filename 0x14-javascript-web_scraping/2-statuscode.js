#!/usr/bin/node
// gets status code from http request

const request = require('request');
let uri = process.argv[2];
if (uri === undefined) {
  console.log('Error: Uszge ./2-statuscode.js <URL>');
} else {
  request.get({ url: uri }, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log('code: ' + response.statusCode);
    }
  });
}
