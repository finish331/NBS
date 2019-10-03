/* eslint-disable no-unused-vars */
const path = require('path')
/* eslint-disable no-unused-vars */
const express = require('express')
const app = express()

const routerapi = require('./router')
const testapi = require('./testApi')
const playerapi = require('./playerApi')
var fs=require("fs");

app.use('/movie', routerapi)
app.use('/test', testapi)
app.use('/player',playerapi)

const db = require('./firbaseInit')
var teamDataTemp = []
db.collection('Player').get().then(teamData => {
    teamData.forEach(doc => {
        teamDataTemp.push(doc.data())
  })
  var myJSON = JSON.stringify(teamDataTemp);
  fs.writeFile("../src/assets/json/player.json", myJSON, "UTF8", function(err) {
    if (err) throw err;
    console.log("檔案寫入操作完成!");
  })
  console.log("檔案寫入操作中 ... ");
});



app.listen(3000)
console.log('success listen at port:3000......')
