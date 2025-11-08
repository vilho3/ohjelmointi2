'use strict';
let num = +prompt("Give a number; ");
if (num >1) {
  for (let i =2; i<num; i++){
    if (num % i === 0) {
      document.querySelector('#target').innerHTML=`${num} is not a prime number`;
    }
    else {
      document.querySelector("#target").innerHTML=`${num} is a prime number`;
    }

  }
}
else {
  document.querySelector("#target").innerHTML=`${num} is not a prime number`;
}
