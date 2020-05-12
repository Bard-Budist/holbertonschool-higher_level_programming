#!/usr/bin/node
const rs = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

rs(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
