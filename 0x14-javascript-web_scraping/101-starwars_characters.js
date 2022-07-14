#!/usr/bin/node

const axios = require('axios');
let tab;
const name = [];

async function start () {
  await axios({
    method: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/'
  }).then(res => {
    if (res) {
      tab = res.data.results;
    }
  });
  const characters = tab[process.argv[2] - 1].characters;
  for (let x = 0; x < characters.length; x++) {
    await axios({
      method: 'GET',
      url: characters[x]
    }).then(r => {
      if (r) {
        name.push(r.data.name);
      }
    });
  }
  name.forEach((element) => {
    console.log(element);
  }
  );
}
start();
