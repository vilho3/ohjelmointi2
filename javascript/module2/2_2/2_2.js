/*
Write a program that asks the user for the number of participants.
After this, the program asks for the names of all participants.
Finally, the program prints the names of the participants on the web page in an ordered list (<ol>) in alphabetical order.*/
const participants=+prompt("Give number of the participants");
let names =[];
for (let i=0; i<participants; i++){
  name=prompt("Give name of participant");
  names.push(name);
}



document.querySelector('#target').innerHTML=names;