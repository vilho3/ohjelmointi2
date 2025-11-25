'use strict';
const source = document.getElementById('source')
const button = document.querySelector('input[type=submit]')
button.addEventListener('click', function(evt){
  evt.preventDefault()
  const name1=document.querySelector('input[name=firstname]').value
  const name2=document.querySelector('input[name=lastname]').value

  const fullname=name1 + " " + name2
  const p = document.querySelector("#target")
  p.textContent= "your name is "+ fullname+"."



})

