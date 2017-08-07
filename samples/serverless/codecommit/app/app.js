var express = require('express')
var bodyParser = require('body-parser')
var moment = require('moment-timezone')

// declare a new express app
var app = express()
app.use(bodyParser.json())

// Enable CORS for all methods
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*")
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
  next()
});

app.get('/time', function(req, res) {
    res.status(200).json({
        "time": moment().tz("CST").format("dddd, MMMM Do YYYY, hh:mm:ss zz")
    });
})

app.get('/time/:tz', function(req, res) {
    var timezone = req.params.tz
    var time = moment().format()
    try {
        time = moment().tz(timezone).format("dddd, MMMM Do YYYY, hh:mm:ss z")
    } catch (ex) {
        console.log(ex)
    }
    res.status(200).json({
        "time": time
    });
})

/*app.listen(3000, function() {
    console.log("App started")
})*/

// Export the app object. When executing the application local this does nothing. However,
// to port it to AWS Lambda we will create a wrapper around that will load the app from 
// this file
module.exports = app