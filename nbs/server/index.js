/* eslint-disable no-unused-vars */
const path = require('path')
/* eslint-disable no-unused-vars */
const express = require('express')

const app = express()
const routerapi = require('./router')

// app.use('/movie', routerapi)

app.get('/movie/getName', (req, res) => {
  res.json({
    data: '後端get Name連接ok'
  })
})

app.listen(3000)
console.log('success listen at port:3000......')
