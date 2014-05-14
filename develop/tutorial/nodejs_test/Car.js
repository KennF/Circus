function Car(config){
    this.name = config.name;
    this.engineSize = config.engineSize;
}

Car.prototype.getEngineSize = function(){
    return this.engineSize;
};

module.exports = Car;