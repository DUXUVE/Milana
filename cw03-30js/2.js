async function name(params) {
    console.log(1);
    await fetch('https://dummyjson.com/todos/1');
    console.log(2);
}
name();
console.log(3);
// Promise.resolve()