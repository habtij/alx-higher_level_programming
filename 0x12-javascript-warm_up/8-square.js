#!/usr/bin/node

const { argv } = require('process');

if (Number(argv[2])) {
  const num = Number(argv[2]);
  let res = '';
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      res += 'X';
    }
    if (i != num - 1) res += '\n';
  }
  console.log(res);
} else {
  console.log('Missing size');
}
