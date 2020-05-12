#!/usr/bin/node
const rs = require('request');

rs(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
