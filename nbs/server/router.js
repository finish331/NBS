const express = require('express')

const app = express()

const db = require('./firbaseInit')

//透過doc('path') 或透過 db.collection('movies').doc('新世紀福爾摩')皆可
app.get('/getName', (req, res) => {
  db.doc('movies/新世紀福爾摩').get().then( doc => {
    res.json({
      data: req.query.ID,
      firbaseData: doc.data().actors
    });
  });
});

module.exports = app
