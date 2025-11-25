'use strict';
document.addEventListener('submit', async function(evt){
  evt.preventDefault();
  const query = document.getElementById('query').value;
  const url = `https://api.tvmaze.com/search/shows?q=${query}`

  try {
    const response = await fetch(url);
    const json = await response.json();
    console.log("search for", query);
    console.log(json);
  } catch (e) {
    console.log('error',e);

  }

});