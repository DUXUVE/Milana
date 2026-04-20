export class ColorSwitch {
  constructor(element, colors, initialColorIndex) {
    this._element = element;
    this._colors = colors;
    this._colorIndex = initialColorIndex;
    this.setColor(initialColorIndex);
    this.addClickHandler();
    
  }

  reset() {
    this.setColor(0);
  }

  setColor(index) {
    if (index < 0 || index > this._colors.length) {
        throw new Error("Color index is out of colors boundaries");
    }
    this._colorIndex = index;
    this._element.style.backgroundColor = this._colors[this._colorIndex];
  }

  addClickHandler() {
    this._element.addEventListener("click", () => {
        this.setColor((this._colorIndex + 1) % this._colors.length);
    //   this._colorIndex++;
    //   if (this._colorIndex >= this._colors.length) {
    //     this._colorIndex = 0;
    //   }
    //   this._element.style.backgroundColor =
    //     this._colors[this._colorIndex];
    });
  }

  getElement() { 
    return this._element; 
}
}
