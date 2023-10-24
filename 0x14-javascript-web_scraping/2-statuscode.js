#!/usr/bin/node
// Send an HTTP request to the specified URL and log the response
// status code to the console.

const request = require('request');
const URL = process.argv[2];

request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
