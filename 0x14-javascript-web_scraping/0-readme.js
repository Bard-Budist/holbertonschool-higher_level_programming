#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (data === undefined) {
    console.log(err);
  } else {
    console.log(data);
  }
});
