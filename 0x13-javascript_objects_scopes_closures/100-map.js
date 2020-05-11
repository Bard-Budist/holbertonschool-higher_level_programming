#!/usr/bin/node
const list = require('./100-data').list;
const new_list = [];
for (const i in list) {
  new_list[i] = list[i] * i;
}
console.log(list);
console.log(new_list);
