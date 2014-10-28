var connect = require('connect');
var logger = require('logger');

function hello() {
    res.end('hello');
}

var app = connect()
  .use(logger(':method :url'))
  .use(hello);
