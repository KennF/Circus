var express = require('express');
var app = express();

app.get("/hello.txt", function(req, res){
    var body = 'Hello world';
    // res.setHeader('Content-Type', 'text/plain');
    // res.setHeader('Content.Length', body.length);
    // res.end(body);
    res.send(body);
});

app.listen(3000);
console.log('listen on port 3000');
