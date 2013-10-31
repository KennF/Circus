var Person = function(name, age, job){
	this.name = name;
	this.age = age;
	this.job = job;
	this.sayName = function(){
		console.log("%s is %s", this.name, this.job);
	};
}

module.exports = Person;