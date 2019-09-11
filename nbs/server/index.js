/* eslint-disable no-unused-vars */
const path = require('path')
/* eslint-disable no-unused-vars */
const express = require('express')
const app = express()

const routerapi = require('./router')
const testapi = require('./testApi')

app.use('/movie', routerapi)
app.use('/test', testapi)

app.listen(3000)
console.log('success listen at port:3000......')
