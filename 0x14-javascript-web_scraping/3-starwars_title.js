#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const num = process.argv[2];

request(url + num, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const resp = JSON.parse(body);
    console.log(resp.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
