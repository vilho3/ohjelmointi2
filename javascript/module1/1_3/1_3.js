'use strict';
let num1=parseInt(prompt("Give number:"));
let num2=parseInt(prompt("Give another number:"));
let num3=parseInt(prompt("Give third number:"));

let sum=num1+num2+num3;
let product=num1*num2*num3;
let average=sum/3;
document.querySelector('#sum').innerHTML='Summary of numbers = ' +sum;
document.querySelector('#product').innerHTML='Product of numbers = ' +product;
document.querySelector('#average').innerHTML='Average of numbers = ' +average;
