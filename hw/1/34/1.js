// 1
let car = {
    manufacturer: "sdgfsg",
    model: "dgdgd",
    year: 2020,
    averageSpeed: 80
};

function showCarInfo(car) {
    console.log("производитель: " + car.manufacturer);
    console.log("модель: " + car.model);
    console.log("год выпуска: " + car.year);
    console.log("средняя скорость: " + car.averageSpeed + " км/ч");
}

function calculateTime(car, distance) {
    let timeWithoutBreaks = distance / car.averageSpeed;
    let breaks = Math.floor(timeWithoutBreaks / 4);
    let totalTime = timeWithoutBreaks + breaks;
    return totalTime;
}

showCarInfo(car);
console.log(calculateTime(car, 500));



// 2
let fraction1 = {
    numerator: 3,
    denominator: 4
};

let fraction2 = {
    numerator: 2,
    denominator: 3
};

// +
function addFractions(f1, f2) {
    let result = {
        numerator: f1.numerator * f2.denominator + f2.numerator * f1.denominator,
        denominator: f1.denominator * f2.denominator
    };
    return result;
}

// -
function subtractFractions(f1, f2) {
    let result = {
        numerator: f1.numerator * f2.denominator - f2.numerator * f1.denominator,
        denominator: f1.denominator * f2.denominator
    };
    return result;
}

// *
function multiplyFractions(f1, f2) {
    let result = {
        numerator: f1.numerator * f2.numerator,
        denominator: f1.denominator * f2.denominator
    };
    return result;
}

// /
function divideFractions(f1, f2) {
    let result = {
        numerator: f1.numerator * f2.denominator,
        denominator: f1.denominator * f2.numerator
    };
    return result;
}

// сокращение
function reduceFraction(fraction) {
    let a = Math.abs(fraction.numerator);
    let b = Math.abs(fraction.denominator);
    while (b) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    let gcd = a;
    let result = {
        numerator: fraction.numerator / gcd,
        denominator: fraction.denominator / gcd
    };
    return result;
}

console.log("сложение: ", addFractions(fraction1, fraction2));
console.log("ыычитание: ", subtractFractions(fraction1, fraction2));
console.log("умножение: ", multiplyFractions(fraction1, fraction2));
console.log("деление: ", divideFractions(fraction1, fraction2));
console.log("сокращение: ", reduceFraction({numerator: 4, denominator: 8}));



// 3
let time = {
    hours: 20,
    minutes: 30,
    seconds: 45
};

function showTime(time) {
    let h = time.hours < 10 ? "0" + time.hours : time.hours;
    let m = time.minutes < 10 ? "0" + time.minutes : time.minutes;
    let s = time.seconds < 10 ? "0" + time.seconds : time.seconds;
    console.log(h + ":" + m + ":" + s);
}

function addSeconds(time, seconds) {
    time.seconds += seconds;
    
    time.minutes += Math.floor(time.seconds / 60);
    time.seconds = time.seconds % 60;
    
    time.hours += Math.floor(time.minutes / 60);
    time.minutes = time.minutes % 60;
    
    time.hours = time.hours % 24;
}

function addMinutes(time, minutes) {
    time.minutes += minutes;
    
    time.hours += Math.floor(time.minutes / 60);
    time.minutes = time.minutes % 60;
    
    time.hours = time.hours % 24;
}

function addHours(time, hours) {
    time.hours += hours;
    time.hours = time.hours % 24;
}

addSeconds(time, 30);
showTime(time);

addMinutes(time, 45);
showTime(time);

addHours(time, 5);
showTime(time);