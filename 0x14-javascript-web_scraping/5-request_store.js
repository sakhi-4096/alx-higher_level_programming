#!/usr/bin/node

// Download content from a given URL and save it to a local file
// specified in the command-line arguments.
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    fs.writeFileSync(process.argv[3], body);
  }
});
