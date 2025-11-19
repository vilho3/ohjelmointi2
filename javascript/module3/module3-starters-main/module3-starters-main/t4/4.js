'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];


let selecti=document.querySelector("#target");

for (let i=0;i<students.length;i++){
  let o=document.createElement("option");
  o.id = students[i].id
  o.textContent=students[i].name
  selecti.appendChild(o)
}