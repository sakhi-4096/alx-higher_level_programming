#!/usr/bin/node

// Define an object called 'myObject' with two properties: 'type' and 'value'
const myObject = {
  type: 'object',
  value: 12
};
// Log the 'myObject' to the console, showing its initial state
console.log(myObject);
// Add a method 'incr' to 'myObject' that increments the 'value' property by 1
myObject.incr = function () {
  this.value += 1;
};

// Call the 'incr' method on 'myObject' to increment 'value' by 1
myObject.incr();
// Log 'myObject' again to show the updated 'value' property
console.log(myObject);
// Call 'incr' method again to increment 'value' once more
myObject.incr();
// Log 'myObject' again to show the further updated 'value' property
console.log(myObject);
// Call 'incr' method one more time to increment 'value' again
myObject.incr();
// Log 'myObject' again to show the final updated 'value' property
console.log(myObject);
