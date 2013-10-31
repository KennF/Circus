var Person = function (name, age, job) {
	this.name = name;
	this.age = age;
	this.job = job;
	// to check on function is enough
	if (typeof this.sayName != "function"){
		Person.prototype.sayName = function(){
			console.log("%s is %s", this.name, this.job);
		}
		Person.prototype.sayAge = function(){
			console.log("age is %d", this.age)
		}
	}

}

module.exports = Person;