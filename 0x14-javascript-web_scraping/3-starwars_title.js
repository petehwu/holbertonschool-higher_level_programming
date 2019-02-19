#!/usr/bin/node
// gets a json and grabs a value

const request = require('request');
request.contentType = 'json';
const uri = 'http://swapi.co/api/films/';
let id = process.argv[2];
if (id === undefined || isNaN(id)) {
  console.log('Error: Usage ./3-strwars_title.js <film_id_number>');
} else {
  request.get({ url: uri + id, json: true }, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(body['title']);
    }
  });
}
