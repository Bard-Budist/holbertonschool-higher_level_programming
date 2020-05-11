#!/usr/bin/node
exports.esrever = function (list) {
  const newList = []; let count = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newList[count] = list[i];
    count++;
  }
  return newList;
};
