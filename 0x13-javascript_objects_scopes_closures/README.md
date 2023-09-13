# JavaScript - Objects, Scopes and Closures
 * JavaScript objects, scopes, and closures are fundamental concepts in the language.

 ![Javascript object](https://res.cloudinary.com/practicaldev/image/fetch/s--b688yBwK--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://833250.smushcdn.com/1694534/wp-content/uploads/2021/06/0_fQTD4DjK71YMUtIS.gif%3Flossy%3D1%26strip%3D1%26webp%3D1)

## Description
 * Understanding objects, scopes, and closures is essential for becoming proficient in JavaScript and writing efficient and maintainable code. These concepts play a crucial role in structuring and organizing your code, managing data, and controlling variable visibility.

## Features
* **Objects:** In JavaScript, objects are composite data types that allow you to store and manipulate data in key-value pairs. Objects are used to represent real-world entities and are a fundamental building
* **Scopes:** JavaScript has two main types of scope: global scope and local (or function) scope. Scope determines the visibility and accessibility of variables and functions within a program.
    * **Global Scope:** Variables declared outside of any function are in the global scope and can be accessed from anywhere in the program.
    * **Local Scope:** Variables declared within a function are in the local scope and can only be accessed within that function. 
* **Closures:** Closures are a powerful and somewhat advanced concept in JavaScript. A closure is formed when a function is defined within another function and has access to the outer function's variables even after the outer function has finished executing. Closures are often used to create private data and encapsulate functionality.

## Usage
```js
// Here's an example of creating and using an object:
const person = {
  firstName: "Sakhile",
  lastName: "Ndlazi",
  age: 16,
  greet: function() {
    console.log(`Hello, my name is ${this.firstName} ${this.lastName}.`);
  }
};

console.log(person.firstName); // Accessing a property
person.greet(); // Calling a method

// Here's an example illustrating scope:
const globalVar = "I'm a global variable";

function exampleFunction() {
  const localVar = "I'm a local variable";
  console.log(globalVar); // Accessing global variable
  console.log(localVar);  // Accessing local variable
}

exampleFunction();
console.log(globalVar); // Accessible here
// console.log(localVar); // This would result in an error, localVar is not defined here

// Here's an example of a closure:
function outer() {
  const outerVar = "I'm from the outer function";

  function inner() {
    console.log(outerVar); // Accessing outer function's variable
  }

  return inner; // Returning the inner function
}

const closureFn = outer(); // The inner function forms a closure
closureFn(); // Executing the closure, still has access to outerVar
```
## Credits
 * [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
 * [Classes in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
 * [Classes ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
 * [super ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 * [extends ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
 * [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
 * [Classes in Javascript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
 * [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
 * [this/self](https://alistapart.com/article/getoutbindingsituations/)
 * [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
