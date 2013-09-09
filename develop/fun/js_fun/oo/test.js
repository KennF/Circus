

console.log("The factory pattern:")
var factory = require('./factoryPattern.js');
var p1 = factory.createPerson("ken", 10, "papa");
var p2 = factory.createPerson("iris", 20, "mama");
p1.sayName();
p2.sayName();

// var p1 = factory("ken", 10, "papa");
// p1.sayName();

console.log("=================================");
console.log("The constructor pattern:")
var Person = require("./constructorPattern");

var p3 = new Person("ken", 1, "papa");
p3.sayName();
console.log(p3 instanceof Person)
console.log(p3.constructor == Person)

console.log("**");
var getGlobal = require("./utils.js")
Person("iris", 2, "mama");
getGlobal().sayName();
console.log(typeof getGlobal())
console.log(getGlobal().constructor)
console.log("**" + "almost the process of how to call a constructor");
var o = new Object();
Person.call(o, "zach", 2, "son");
o.sayName();
console.log(o instanceof Person)
console.log(o.constructor == Object)
console.log(o.constructor == Person)

console.log("=================================");
console.log("The prototype pattern:")
var ProtoPerson = require("./prototypePattern");
var p = new ProtoPerson();
p.sayName();
console.log(ProtoPerson.prototype.isPrototypeOf(p));
console.log(Object.getPrototypeOf(p) == ProtoPerson.prototype);
// console.log(p.getPrototypeOf() == ProtoPerson.prototype);
// getPrototypeOf should be the method on Object, not on its prototype
console.log(p.hasPrototypeProperty(p, "name"));
p.name = "iris";
console.log(p.hasPrototypeProperty(p, "name"));
delete p.name;
console.log(p.hasPrototypeProperty(p, "name"));

console.log("=================================");
console.log("The combine constructor and prototype pattern:")
var Combine = require("./combineConstructorPrototype.js");
var c = new Combine("ken", 12, "papa");
c.sayName()
c.sayAge();
var c1 = new Combine("iris", 13, "mama");
console.log(c.sayName == c1.sayName);