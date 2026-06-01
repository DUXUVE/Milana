import { Carousel } from "./Carousel/carousel.js";

new Carousel(document.querySelector(".carousel"), [...document.querySelectorAll(".images")], 1000);
