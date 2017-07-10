var express = require('express');
var port = process.env.PORT || 3000;
var app = express(),
path = require('path'),
publicDir = path.join(__dirname,'public');

app.use(express.static(publicDir))

app.listen(port);
