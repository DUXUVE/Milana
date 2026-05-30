const image = document.querySelector(".image-container");
const position = {x: 0, y: 0};
const screenSizes = {width: window.innerWidth, height: window.innerHeight};
const speed = {x: 10, y: 10};
let hueRotation = 0;
const minHueRotation = 72;
const maxHueRotation = 270;
function render() {
    if (
        position.x + speed.x < 0 ||
        position.x + image.clientWidth + speed.x >= screenSizes.width
    ) {
        hueRotation = 
            Math.random() * (maxHueRotation - minHueRotation) + minHueRotation;
        image.style.filter = `hue-rotate(${hueRotation}deg)`;
        position.x = speed.x > 0 ? screenSizes.width - image.clientWidth : 0;
        speed.x *= -1;
    } else {
        position.x += speed.x;
    }
    image.style.left = `${position.x}px`;
    if (
        position.y + speed.y < 0 ||
        position.y + image.clientHeight + speed.y >= screenSizes.height
    ) {
        hueRotation = 
            Math.random() * (maxHueRotation - minHueRotation) + minHueRotation;
        image.style.filter = `hue-rotate(${hueRotation}deg)`;
        position.y = speed.y > 0 ? screenSizes.height - image.clientHeight : 0;
        speed.y *= -1;
    } else {
        position.y += speed.y;
    }
    image.style.top = `${position.y}px`;
    requestAnimationFrame(render);
}
render();