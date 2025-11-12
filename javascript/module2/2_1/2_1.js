'use strict';
const numbers = [];
let range = 5;
for (let i=0; i<range; i++) {
  let numerot=+prompt("Give a number: ");
  numbers.push(numerot);
}
let reverse=[];
for (let i =numbers.length-1; i>=0;i--){
  reverse.push(numbers[i])


}
document.querySelector('#target').innerHTML=`numbers in reverse: ${reverse}`;
