/* eslint-disable no-unused-vars */
const path = require('path')
/* eslint-disable no-unused-vars */
const express = require('express')

const app = express()
const routerapi = require('./router')

const admin = require('firebase-admin');
const serviceAccount = require('../../../project_key/ServerKey.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

var t = 123

// app.use('/movie', routerapi)

app.get('/movie/getName', (req, res) => {
  db.collection('movies').doc('新世紀福爾摩').get().then(function(doc){
    res.json({
      data: req.query.ID
    });
  });
});

async function test(){
  db.collection('movies').doc('新世紀福爾摩').get().then(function(doc){
    t = doc.data().date
    console.log(t);
  });
}

app.listen(3000)
console.log('success listen at port:3000......')
