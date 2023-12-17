#!/usr/bin/node

const { argv } = require('process');

if (argv.length <= 3) {
  console.log(0);
}

let list = [];
for (let i = 2, j = 0; i <= argv.length; i++, j++) {
  list[j] = argv[i];
}
list.sort(function (a, b) { return (b - a) });
console.log(list[-2]);
