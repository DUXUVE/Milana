console.log(1);

setTimeout(() => {
  console.log(2);

  Promise.resolve().then(() => {
    console.log(3);
  });

  queueMicrotask(() => { // микрозадача
    console.log(4);
  });

  setTimeout(() => {
    console.log(5);
  }, 0);
}, 0);

async function test() {
  console.log(6);

  await Promise.resolve();

  console.log(7);

  setTimeout(() => {
    console.log(8);
  }, 0);
}

test();

Promise.resolve().then(() => {
  console.log(9);
});

queueMicrotask(() => { // микрозадача
  console.log(10);
});

console.log(11);

// 1 6 7 11 9 2 3 4 8 5