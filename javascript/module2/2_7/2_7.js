/*
Modify the function above so that it gets the number of sides on the dice as a parameter.
With the modified function you can for example roll a 21-sided role-playing dice.
The difference to the last exercise is that the dice rolling in the main program continues
until the program gets the maximum number on the dice, which is asked from the user at the beginning. (2p)
 */

let matti=true;
let list=[];
const sides= +prompt("GIVE NUMBER OF SIDE: ")

function roll() {
  let number = Math.floor(Math.random() * sides)+1;
  return number;
}

while (matti){
  number=roll();
  list.push(number);
  if (number===sides){
    matti=false;
  }
}




let ul = document.querySelector("#target");

for (let i=0; i<list.length; i++){
  const li = document.createElement("li");
  li.textContent = list[i];
  ul.appendChild(li);
}