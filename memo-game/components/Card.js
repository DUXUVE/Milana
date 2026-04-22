import { ColorSwitch } from "../../../memo-game/components/colorSwitch";

export class CardElement {
    constructor(element, colorWhenHiden, colorWhenShowd) {
        this._element = element;
        this._switch = new ColorSwitch(this._element, [colorWhenHiden, colorWhenShowd], 0);
    }

    show() {

    }

    hide() {

    }
    
    getElement() {
        return this._element;
    }
}