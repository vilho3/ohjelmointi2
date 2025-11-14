/*
Write a program that prompts the user for numbers. When the user enters one of the numbers previously entered,
the program will announce that the number has already been given and stops its operation and
then prints all the given numbers to the console in ascending order. (2p)
 */
'use strict';
let matti = true;
let numbers=[];

while (matti){
  let number=+prompt("GIVE NUMBER: ");
  numbers.push(number)
  if (number in numbers) {
    alert("THIS NUMBER HAS BEEN GIVEN");
    matti=false;
  }
}
numbers.sort((a,b) => a-b)
for (let i in numbers){
  console.log(numbers[i])
}