'use strict';

async function funktionnimi() {
  try {
    const url = `https://api.chucknorris.io/jokes/random`;
    const response = await fetch(url);
    const json = await response.json();
    const value = json.value;
    console.log(value);

  } catch (e) {
    console.log('ERROR', e);
  }

}

funktionnimi()
