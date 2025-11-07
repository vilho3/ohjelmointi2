'use strict';
const dice=+prompt("Give number of dice: ")
let sum=0;

for (let i=0; i< dice ; i++) {
  let number = Math.floor(Math.random()* 6 ) + 1;
  sum +=number;
}
document.querySelector('#target').innerHTML=`throwing ${dice} dice`;
document.querySelector('#target2').innerHTML=`summary of numbers is ${sum}`;