class Car {
    constructor(brand, model) {
        this.brand = brand;
        this.model = model;
    }

    getFullName() {
        return this.brand + " " + this.model;
    }
}

class Garage {
    constructor(capacity) {
        this.capacity = capacity;
        this.cars = [];
    }

    parkCar(car) {
        if (this.cars.length < this.capacity) {
            this.cars.push(car);
            console.log("машина " + car.getFullName() + " припаркована");
            return {slot: this.parkCar.length - 1, error: null};
        }
        else {
            console.log("мест нет, " + car.getFullName() + " не поместилась");
            return { slot: null, error: "гараж полон"};
        }
    }

    showParkedCars() {
        console.log("сейчас в гараже:");
        for (let i = 0; i < this.cars.length; i++) {
            console.log(this.cars[i].getFullName());
        }
    }
}

const garage = new Garage(2);
const car1 = new Car("BMW", "X5");
const car2 = new Car("Toyota", "Camry");
const car3 = new Car("Lada", "Vesta");

garage.parkCar(car1);
garage.parkCar(car2);
garage.parkCar(car3);

garage.showParkedCars();