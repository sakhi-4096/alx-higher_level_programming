#!/usr/bin/node

// Import the 'fs' module to work with the file system
const fs = require('fs');

// Get the filename from the command line arguments
const file = process.argv[2];

// Read the content of the file using 'fs.readFile' method
fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    // If there's an error, log it to the console
    console.log(err);
  } else {
    // If successful, log the file's content to the console
    console.log(data);
  }
});
