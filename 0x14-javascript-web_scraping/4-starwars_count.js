#!/usr/bin/node
// gets a json and grabs a value

const request = require('request');
const uri = process.argv[2];
let count = 0;
let search = new RegExp('https://swapi.co/api/people/18/');
if (uri === undefined) {
  console.log('Error: Usage ./4-starwars_count.js <starwars_api_url>');
} else {
  request.get({ url: uri, json: true }, function (error, response, body) {
    if (error || response.statusCode !== 200) {
      console.log('0');
    } else {
      let index = 0;
      for (index = 0; index < body.results.length; index++) {
        let joined = body.results[index].characters.join();
        if (search.test(joined)) {
          count++;
        }
      }
      console.log(count.toString());
    }
  });
}
