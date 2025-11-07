'use strict';
const start = +prompt("Give start year: ");
const end = +prompt("Give end year: ");
const list=document.getElementById("target");

for (let i=start; i <end; i++) {
  if ((i % 4 ===0 && i % 100 !==0) ||(i % 400=== 0)){
    const li =document.createElement("li");
    li.textContent=i;
    list.appendChild(li);

  }
}


