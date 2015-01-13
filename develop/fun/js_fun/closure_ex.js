name = "The window";

var obj1 = {
    name: 'My obj1',
    getNameFunc: function() {
        return function () {
            return this.name;
        };
    }
};

console.log(obj1.getNameFunc()());


var obj2 = {
    name: 'My obj2',
    getNameFunc: function() {
        var that = this;
        return function () {
            return that.name;
        };
    }
};
console.log(obj2.getNameFunc()());

