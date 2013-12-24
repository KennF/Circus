var http = require('http');
var util = require('util');
var url = require('url');

var server = new http.Server();
server.on('request', function (req, res) {
    res.writeHead(200, { "content-type": "text/plain"});
    // res.write(req.client);
    // res.write(req.method);
    // res.write(req.headers);
    res.write(req.httpVersion + '\n');
    res.end(util.inspect(url.parse(req.url, true), true));

});
server.listen(1235);

console.log('server starts at port 1235');
