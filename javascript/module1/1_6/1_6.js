'use strict';
const answer = confirm('Should i calculate the square root? ');
if (answer === true) {
  let number =+prompt("Give a number: ");
  if (number < 0){
    document.querySelector('#target').innerHTML=`The square root of a negative number is not defined`
  }
  else {
    let square = number**(1/2);
    document.querySelector('#target').innerHTML=`square root of ${number} is: ${square}`;
  }

}
if (answer === false) {
  document.querySelector('#target').innerHTML=`Square root is not calculated`;
}