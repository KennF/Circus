function Hello() {
    this.world = function() {
        console.log('hello world');
    };
}

module.exports = Hello;
