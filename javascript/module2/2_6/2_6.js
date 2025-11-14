/*
Write a function that returns a random dice roll between 1 and 6.
The function should not have any parameters. Write a main program that rolls the dice until the result is 6.
The main program should print out the result of each roll in an unordered list (<ul>). (2p)
 */
let matti=true;
let list=[];

function roll() {
  let number = Math.floor(Math.random() * 6)+1;
  return number;
}

while (matti){
  number=roll();
  list.push(number);
  if (number===6){
    matti=false;
  }
}




let ul = document.querySelector("#target");

for (let i=0; i<list.length; i++){
  const li = document.createElement("li");
  li.textContent = list[i];
  ul.appendChild(li);
}