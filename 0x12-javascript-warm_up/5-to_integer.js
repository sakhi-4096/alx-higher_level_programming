#!/usr/bin/node
/* Print number converted to an integer */

const arg = parseInt(process.argv[2], 10);
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${arg}`);
}
