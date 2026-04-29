"use strict";

class ColorSwitcher {
  constructor(element) {
    this.colorIndex = 0;
    this._element = element;
    this.addClickHandler();
    // this._element.style.width = "100px";
    // this._element.style.height = "100px";
    this._element.style.backgroundColor = ColorSwitcher.backgroundColors[this.colorIndex];
  }

  static backgroundColors = ["red", "blue", "green"];

  addClickHandler() {
    this._element.addEventListener("click", () => {
      this.colorIndex++;
      if (this.colorIndex == ColorSwitcher.backgroundColors.length) {
        this.colorIndex = 0;
      }
      this._element.style.backgroundColor =
        ColorSwitcher.backgroundColors[this.colorIndex];
      // this.style.backgroundColor = `${colorList[i]}`;
    });
  }

  getElement() { 
    return this._element; 
}
}

// const switcher = new ColorSwitcher(
//   document.getElementById("button-switcher-color"),
// );

const blockList = document.querySelector(".block-list");
const switchers = [];
const switchersCount = 4 * 4;

for (let i = 0; i <switchersCount; i++) {
    const element = document.createElement("div");
    element.classList.add("colored-block");
    const switcher = new ColorSwitcher(element);
    switchers.push(switcher);
    blockList.appendChild(switcher.getElement());
}
