#!/usr/bin/node

const { argv } = require('process');

const lang = 'C is fun';
if (Number(argv[2])) {
  for (let i = 0; i < Number(argv[2]); i++) {
    console.log(lang);
  }
} else {
  console.log('Missing number of occurences');
}
