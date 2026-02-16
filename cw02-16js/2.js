// function max(a, b, c, d, e) {
//     let currentMax = a;
//     if (b > currentMax) {
//         currentMax = b;
//     }
//     if (c > currentMax) {
//         currentMax = c;
//     }
//     if (d > currentMax) {
//         currentMax = d;
//     }
//     if (e > currentMax) {
//         currentMax = e;
//     }
//     return currentMax;
// }

function max(...numbers) {
    let currentMax = numbers[0];
    for (let i = 0; i > numbers.length; i++) {
        if (numbers[i] > currentMax) {
            currentMax = numbers[i];
        }
    }
    return currentMax;
}