/*
Write a program that asks the user for numbers until the user gives zero.
The given numbers are printed in the console from the largest to the smallest. (2p)
 */
'use strict';
let numbers=[];
let matti=true;

while (matti){
  let number = +prompt("Give number:");
  numbers.push(number)
  if (number === 0) {
    matti = false;
  }

}
numbers.sort((a,b) => b-a);
for (let i in numbers) {
  console.log(numbers[i])
}