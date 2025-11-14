
'use strict';
let list=[]
const candidates =+prompt("GIVE NUMBER OF THE CANDIDATES");
for (let i=0; i<candidates;i++){
  let name=prompt(`GIVE NAME OF ${i+1} CANDIDATE`);
  list.push({
    name: name,
    votes: 0
  });
}
const voters = +prompt("GIVE AMOUNT OF VOTERS!!!");
for (let i=0; i<voters;i++){
  let vote = prompt("GIVE YOUR VOTE!!!!");
  for (let i=0; i<list.length;i++){
    if (list[i].name ===vote){
      list[i].votes+=1;
    }
  }
}

list.sort((a, b) => b.votes - a.votes);
console.log(`winner is ${list[0].name} with ${list[0].votes} votes`);

for (let i=0; i<list.length;i++){
  console.log(`${list[i].name}: ${list[i].votes} votes `)
}

