#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');
// Get the episode number from the command line arguments
const episodeNum = process.argv[2];
// Define the API URL for the Star Wars API
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

// Send an HTTP request to the specified episode's API URL
request(API_URL + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
