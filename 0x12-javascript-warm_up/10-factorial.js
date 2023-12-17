#!/usr/bin/node

const { argv } = require('process');

function factorial (n) {
  if (isNaN(Number(n)) || Number(n) === 0 || Number(n) === 1) {
    return (1);
  }
  return (Number(n) * factorial(Number(n) - 1));
}

console.log(factorial(argv[2]));
