const num1 = document.getElementById("num1");
const num2 = document.getElementById("num2");

const button = document.getElementById("start");
const p =document.querySelector("#result")
const operatinos =document.getElementById('operation')
button.addEventListener('click',function(){
  let a = parseFloat(num1.value)
  let b = parseFloat(num2.value)
  let result;

  if (operatinos.value==='add'){
    result = a + b
  }
  else if (operatinos.value==='sub'){
    result= a-b
  }
  else if (operatinos.value==='multi'){
    result= a*b
  }
  else if (operatinos.value==='div'){
    result= a/b
  }
  p.textContent=result;

})