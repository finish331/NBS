const express = require('express')

const app = express()

const db = require('./firbaseInit')

app.get('/testWhere', (req, res) => {
  var temp = []
  db.collection('test_collection').where('data', '==', '1').get().then(snapShot => {
    snapShot.forEach(doc => {
      temp.push(doc.data().data)
    })
    res.json({
      firbaseData: temp
    });
  });
});

module.exports = app