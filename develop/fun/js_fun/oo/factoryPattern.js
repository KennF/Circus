var createPerson = function(name, age, job){
	var o = new Object();
	o.name = name;
	o.age = age;
	o.job = job;
	o.sayName = function(){
		console.log("createPerson:%s is %s!!", this.name, this.job);
	};
	return o;
}

// var createPerson1 = function(name, age, job){
// 	var o = new Object();
// 	o.name = name;
// 	o.age = age;
// 	o.job = job;
// 	o.sayName = function(){
// 		console.log("createPerson1:%s is %s!!", this.name, this.job);
// 	};
// 	return o;
// }

module.exports = {
  createPerson: createPerson
};

// module.exports = createPerson;
// module.exports = createPerson1;
// the later export will hide the first one!!!


