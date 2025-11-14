/*
Write a function called concat(), which receives an array of strings as a parameter.
The function returns a string formed by concatenating the elements of the array. (2p)
Example: In a four-item array, there are items Johnny, DeeDee, Joey and Marky.
The function returns the string JohnnyDeeDeeJoeyMarky.

Do not use array.join() function
You can hardcode the array, no need for prompt().
Print the result to HTML document.
 */
'use strict';
let arrayy = ['Johnny', 'DeeDee', 'Joey', 'Marky']

function concat(arrayy){
  let list=[];
  for (let name in arrayy){
    list += arrayy[name];
  }
  return list;
}

let lista = concat(arrayy);

document.querySelector("#target").innerHTML=arrayy;
document.querySelector("#targett").innerHTML=lista;