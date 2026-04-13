export class CounterButton {
    constructor(caption, valueChangeOnClick) {
        this._element = document.createElement('button');
        this._element.addEventListener(this.onClick);
    }
    onClick() {
        valueUpdater();
    }
}