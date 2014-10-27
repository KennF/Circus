var events = require('events')
  , net = require('net');

var channel = new events.EventEmitter();
channel.clients = {};
channel.subscriptions = {};

channel.on('join', function(id, client) {
    this.clients[id] = client; 
    this.broadcast = function(senderId, message) {
    // if (id != senderId) { 
    //   this.clients[id].write(message);
    // }
    // console.log(util.inspect(this.clients, false, null));
    // console.log(util.inspect(this.subscriptions, false, null));
    // for (var client in clients) {
    //     client.write(message);
    // }
    console.log(senderId + ' broadcast: ' + message);
  }
  this.on('broadcast', this.broadcast); 
  // console.log(Object.keys(this.clients).length);
  // console.log(Object.keys(this.subscriptions).length);
});

var server = net.createServer(function (client) {
    var id  = client.remoteAddress + ':' + client.remotePort;
    console.log(id);  

    client.on('connect', function() {
        
        channel.emit('join', id, client);
        console.log(id + ' join');
    });

    client.on('data', function(data) {
        console.log(id + ' says: ' + data);
        channel.emit('broadcast', id, data);
        console.log('done');
    });
});

server.listen(2345);