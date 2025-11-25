'use strict';
document.addEventListener('submit', async function(evt){
  evt.preventDefault();
  const query = document.getElementById('query').value;
  const url = `https://api.tvmaze.com/search/shows?q=${query}`

  try {
    const response = await fetch(url);
    const json = await response.json();
    const div= document.getElementById('results');
    div.innerHTML='';
    for (let i=0; i < json.length;i++){
      const vastaus=json[i].show
      const article = document.createElement('article');
      const name = document.createElement('h2');
      name.textContent=vastaus.name;
      article.appendChild(name);
      const link=document.createElement('a');
      link.href=vastaus.url;
      link.textContent="link"
      link.target="_blank";   
      article.appendChild(link);

      const img=document.createElement('img');
      if (vastaus.image) {
        img.src=vastaus.image.medium
      } else {
        img.src=`https://placehold.co/210x295?text=Not%20Found`
      }
      img.alt=vastaus.name
      article.appendChild(img)

      const summary = document.createElement('div');
      summary.innerHTML=vastaus.summary;
      article.appendChild(summary);
      div.appendChild(article)


    }


  } catch (e) {
    console.log('error',e);

  }

});