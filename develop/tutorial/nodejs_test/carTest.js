var should = require('should');
var car = require("./Car.js");
var assert = require("assert");

var myCar = new car({
    name: "vitz",
    engineSize: 1000
});

describe('#Car()', function(){
    it('Car engineSize method test', function(){
        myCar.getEngineSize().should.equal(1000);
    })
})

describe('#Car()', function(){
    it('Car engineSize method test - negative', function(){
        myCar.getEngineSize().should.equal(1000);
    })
})

describe('#Car()', function(){
    it('Car name test', function(){
        myCar.name.should.equal("vitz");
    })
})

