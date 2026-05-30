const trafficLight = document.createElement("div");
trafficLight.classList.add("traffic-lights");
const container = document.querySelector(".container");
container.appendChild(trafficLight);
const lights = [];
for (let index = 0; index < 3; index++) {
    lights.push(document.createElement("div"));
    lights[index].classList.add("light");
    trafficLight.appendChild(lights[index]);
}

// const lights = document.querySelectorAll(".light");

// lights[0].style.backgroundColor="red";
// lights[1].style.backgroundColor="yellow";
// lights[2].style.backgroundColor="green";

lights[0].dataset.color="red";
lights[1].dataset.color="yellow";
lights[2].dataset.color="green";

let n = 0;
setInterval(function() {
    lights[n].style.backgroundColor = lights[n].dataset.color;
    lights[n > 0? n - 1: lights.length - 1].style.backgroundColor = "";
    n = (n+1)%lights.length;
}, 1000);