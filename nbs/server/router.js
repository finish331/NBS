const express = require('express')

const router = express.Router()
// const api = require('./api')

router.get('/getName', (req, res) => {
  res.json({
    data: '後端get Name連接ok'
  })
})

module.exports = router
