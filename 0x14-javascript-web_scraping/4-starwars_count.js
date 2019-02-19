#!/usr/bin/node
// gets a json and grabs a value

const request = require('request');
request.contentType = 'json';
const uri = process.argv[2];
let count = 0;
if (uri === undefined) {
  console.log('Error: Usage ./4-starwars_count.js <film_id_number>');
} else {
  request.get({ url: uri, json: true }, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let res = body.results;
      let index = 0;
      for (index = 0; index < res.length; index++) {
        if (res[index].characters.includes('https://swapi.co/api/people/18/')) {
          count++;
        }
      }
      console.log(count);
    }
  });
}
