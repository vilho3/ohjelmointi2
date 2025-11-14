
const participants=+6;
let names =[];
for (let i=0; i<participants; i++){
  name=prompt("Give name of dog");
  names.push(name);
}
names.sort().reverse() 
const list =document.getElementById("target")

for (let i=0; i<names.length; i++){
  const li = document.createElement("li");
  li.textContent=names[i]
  list.appendChild(li);

}

