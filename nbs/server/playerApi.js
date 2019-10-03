const express = require('express')

const app = express()

const db = require('./firbaseInit')

//透過doc('path') 或透過 db.collection('movies').doc('新世紀福爾摩')皆可
app.get('/getPlayer', (req, res) => {
    var temp = []
    db.collection('Player').get().then(snapShot => {
      snapShot.forEach(doc => {
        temp.push(doc.data())
      })
      res.json({
        firbaseData: temp
      });
    });
  });
  

module.exports = app