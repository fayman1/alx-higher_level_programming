#!/usr/bin/node
function factorial (p) {
  return p === 0 || isNaN(p) ? 1 : p * factorial(p - 1);
}

console.log(factorial(Number(process.argv[2])));
