'use strict';
const dice=+prompt("Give number of dice: ")
const ask_sum=+prompt("Give sum of the numbers: ")
let counter =0;
const range=100000;

for (let i=0; i<range; i++){
  let sum=0
  for (let i=0; i< dice ; i++) {
    let number = Math.floor(Math.random()* 6 ) + 1;
    sum +=number;
  }
  if (sum === ask_sum){
    counter+=1;
  }
}
const probability = (counter/range)*100;

document.querySelector('#target').innerHTML= `${dice} dice, sum ${ask_sum}, probability is about ${probability.toFixed(1)}%`;