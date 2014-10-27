function asyncFunction(callback) {
  setTimeout(callback, 200);
}
color = 'blue';
asyncFunction(function() {
console.log('The color is ' + color);
});
color = 'green';
