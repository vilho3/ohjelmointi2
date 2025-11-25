'use strict';
document.addEventListener('submit',async function(evt){
  evt.preventDefault()
  const query = document.getElementById('query').value
  const url = `https://api.chucknorris.io/jokes/search?query=${query}`;
  const div=document.getElementById("target")

  try {
    const response = await fetch(url);
    const json = await response.json();

    for (let i=0; i<json.result.length;i++){
      const text=json.result[i].value
      const article = document.createElement('article');
      const p = document.createElement('p');
      p.textContent=text
      article.appendChild(p)

      div.appendChild(article)

    }

  } catch (e) {
    console.log('ERROR', e);
  }
})



