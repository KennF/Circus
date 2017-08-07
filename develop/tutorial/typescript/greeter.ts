function greeter(person: Person) {
    return "Hello, " + person. firstName + " " + person.lastName;
}

class Student {
    fullName: String;
    constructor(public firstName, public middle, public lastName) {
        this.fullName = firstName + " " + middle + " " + lastName;
    }
}

interface Person {
    firstName: String;
    lastName: String;
}

// var user = "Jane User";
// var user = [0, 1, 2];

// var user = { firstName: "Jane", lastName: "User"};
var user = new Student("Jane", "M.", "User")

console.log(user);
console.log(greeter(user));
