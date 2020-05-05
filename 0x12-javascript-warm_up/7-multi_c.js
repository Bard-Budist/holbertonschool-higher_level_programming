#!/usr/bin/node
const value = parseInt(process.argv[2], 10);
if (isNaN(value)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < value; i++) {
    console.log('C is fun');
  }
}
