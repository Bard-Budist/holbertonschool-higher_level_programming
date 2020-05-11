#!/usr/bin/node
const list = require('./100-data').list;
const new_list = [];
for (const y in list) {
  new_list[y] = list[y] * y;
}
console.log(list);
console.log(new_list);
