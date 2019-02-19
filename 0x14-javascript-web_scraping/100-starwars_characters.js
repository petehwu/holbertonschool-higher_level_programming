#!/usr/bin/node
// gets a json and grabs some values

const request = require('request');
request.contentType = 'json';
const uri = 'http://swapi.co/api/films/';
let id = process.argv[2];
if (id === undefined || isNaN(id)) {
  console.log('Error: Usage ./100-starwars_characters.js <film_id_number>');
} else {
  request.get({ url: uri + id, json: true }, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let chars = body.characters;
      chars.forEach(function (c) {
        request.get({ url: c, json: true }, function (error, response, body) {
          if (error) {
            console.log(error);
          } else {
            console.log(body.name);
          }
        });
      });
    }
  });
}
