/*
Write a function called even(), which receives an array containing numbers as a parameter.
The function returns a second (usually smaller) array which has the even numbers of the original array.
The function must not make changes to the original array. (3p)
Example: In a three-item array, there are items 2, 7 and 4. The function returns a two-item array with items 2 and 4.
Print both the original array and the new array to the console in the main program after you have called the function.
You can hard code the array, no need for prompt().
 */
'use strict';
let arrayy=[2,4,7]

function even(arrayy){
  let list=[]
  for (let i in arrayy){
    if (arrayy[i] % 2 ===0){
      list.push(arrayy[i])
    }
  }
  return list;
}

let lista = even(arrayy)
console.log(arrayy)
console.log(lista)

document.querySelector("#target").innerHTML=arrayy
document.querySelector("#targett").innerHTML=lista