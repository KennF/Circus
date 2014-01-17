var hello1 = require('./module');
hello1.setName('test');
hello1.sayHello();

var hello2 = require('./module');
hello2.setName('testken');
hello2.sayHello();

var Hello = require('./somepackage');
hw = new Hello();
hw.world();
