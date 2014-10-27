var currency = require('./currency');
var util = require('util');

console.log(util.format('50 Canadian dollars equals to %s US dollars', currency.canadianToUS(50)));
console.log(util.format('30 US dollars equals to %s Canadian dollars', currency.usToCanadian(30)));