var Person = function () {
};
Person.prototype.name = "ken";
Person.prototype.age = 10;
Person.prototype.job = "papa";
Person.prototype.sayName = function(){
	console.log("%s is %s", this.name, this.job);
};

Object.prototype.hasPrototypeProperty = function(object, name) {
	return !object.hasOwnProperty(name) && (name in object);
};

module.exports = Person;