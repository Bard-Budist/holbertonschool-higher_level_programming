#!/usr/bin/node
const list = require('./100-data').list;
let count = 0;
const newList = list.map(x => x * count++);
console.log(list);
console.log(newList);
