var util = require('util');

function Base () {
    this.name = "base";
    this.base = 1983;
    this.sayHello = function () {
        console.log('Hello, ' + this.name);
    };

}
Base.prototype.showName = function () {
    console.log(this.name);
};

function Sub () {
    this.name = "Sub";
}

util.inherits(Sub, Base);

var base = new Base();
base.sayHello();
base.showName();

var sub = new Sub();
// sub.sayHello();
sub.showName();

function Person () {
    this.name = "ken";

    this.toString = function () {
        console.log(this.name);
    };
}

var obj = new Person();

console.log(util.inspect(obj));
console.log(util.inspect(obj, true));
