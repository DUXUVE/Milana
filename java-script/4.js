`use strict`;

const hours = +prompt("hours: ");
const minutes = +prompt("minutes: ");
const seconds = +prompt("seconds: ");

if (hours >= 0 && hours <= 23) {
    console.log("1")
}
else {
    console.log("0")
}

if (minutes >= 0 && minutes <= 59) {
    console.log("1")
}
else {
    console.log("0")
}

if (seconds >= 0 && seconds <= 59) {
    console.log("1")
}
else {
    console.log("0")
}
