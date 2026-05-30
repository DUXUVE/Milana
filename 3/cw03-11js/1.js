function GasStation(storedFuel) {
    this.storedFuel = storedFuel;
}
function Car(name, tankCapacity, fuelNow) {
    this.name = name;
    this.tankCapacity = tankCapacity;
    this.fuelNow = fuelNow;
}
Car.prototype.tryAddFuel = function (fuelAmount) {
    const freeSpace = this.tankCapacity - this.fuelNow;
    if ()

}

const car1 = new Car("sds", 40, 12);
const station = new GasStation("fhf", 100);