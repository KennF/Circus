var async = require('async');

// create a queue object with concurrency 2
var concurrency = 0;

var q = async.queue(function (task, callback) {
    console.log('hello ' + task.name);
    concurrency++;
    console.log('concurrency is', concurrency);
    callback();
}, 3);


// assign a callback
q.drain = function() {
    console.log('all items have been processed');
}

// add some items to the queue

q.push({name: 'foo'}, function (err) {
    console.log('finished processing foo');
    concurrency--;
    console.log('concurrency is', concurrency);
});
q.push({name: 'bar'}, function (err) {
    console.log('finished processing bar');
    concurrency--;
    console.log('concurrency is', concurrency);
});

// add some items to the queue (batch-wise)

q.push([{name: 'baz'},{name: 'bay'},{name: 'bax'}], function (err) {
    console.log('finished processing ba*');
    concurrency--;
    console.log('concurrency is', concurrency);
});

// add some items to the front of the queue

q.unshift({name: 'bar'}, function (err) {
    console.log('finished processing bar');
    concurrency--;
    console.log('concurrency is', concurrency);
});