let square = document.getElementById("square");
let size = 50; 
let x = 0;
let y = 0;
let speed = 5; 
let grow = 0.3;
let side = "top";

function animate() {
    if (side === "top") {
        x = x + speed;
        if (x + size >= window.innerWidth) {
            side = "right";
            x = window.innerWidth - size;
        }
    } 
    else if (side === "right") {
        y = y + speed;
        if (y + size >= window.innerHeight) {
            side = "bottom";
            y = window.innerHeight - size;
        }
    } 
    else if (side === "bottom") {
        x = x - speed;
        if (x <= 0) {
            side = "left";
            x = 0;
        }
    } 
    else if (side === "left") {
        y = y - speed;
        if (y <= 0) {
            side = "top";
            y = 0;
        }
    }

    size = size + grow;

    square.style.width = size + "px";
    square.style.height = size + "px";
    square.style.left = x + "px";
    square.style.top = y + "px";

    if (size < window.innerWidth && size < window.innerHeight) {
        requestAnimationFrame(animate);
    } else {
        square.style.width = "100%";
        square.style.height = "100%";
        square.style.left = "0px";
        square.style.top = "0px";
    }
}

animate();