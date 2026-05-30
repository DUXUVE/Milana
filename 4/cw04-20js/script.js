"use strict";

import { ColorSwitch } from "./colorSwitch.js";

const blockList = document.querySelector(".block-list");
const switchers = [];
const switchersCount = 4 * 4;

for (let i = 0; i <switchersCount; i++) {
    const element = document.createElement("div");
    element.classList.add("colored-block");
    const switcher = new ColorSwitch(element, 
      ["hsl(0, 70%, 80%)", "hsl(180, 70%, 80%)"], 
      Math.floor(Math.random() * 2));
    switchers.push(switcher);
    blockList.appendChild(switcher.getElement());
}
