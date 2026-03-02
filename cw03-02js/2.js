// function welcome() {
//     return "Hello";
// }
// console.log(welcome());


// function getUserWelcome(name) {
//     return `Hello, ${name}`;
// }
// console.log(getUserWelcome("sfs"));


// function age(yearNow, yearBirth) {
//     return yearNow - yearBirth;
// }
// console.log(age(2026, 2007));


// function a(a, b) {
//     return b - a;
// }
// console.log(a(3, 2));


// function b(a) {
//     return a * a;
// }
// console.log(b(3));


// function fullName(name, surname) {
//     return `${name} ${surname}`;
// }
// console.log(fullName("dsg","dsfsd"));


// function max(a, b) {
//     if (a > b) {
//         return a;
//     }
//     else {
//         return b;
//     }
// }
// console.log(max(2, 4));


// function arithmeticMean(a, b, c) {
//     return (a + b + c) / 3;
// }
// console.log(arithmeticMean(2, 3, 5));


// function totalCost(cost, discount) {
//     return cost - (cost * (discount / 100));
// }
// console.log(totalCost(100, 20));


// function kmToMeters(km) {
//     return km * 1000;
// }
// console.log(kmToMeters(32));


function isValidPassword(password) {
    if (password.length > 8) {
        return true
    }
    else {
        return false
    }
}
console.log(isValidPassword("54532435"));


