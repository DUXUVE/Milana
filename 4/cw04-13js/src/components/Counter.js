import { Counter } from "./CounterController.js";
export class Counter {
    constructor() {
        this._controller = new CounterController();
        this._element = this._createRoot(this._controller);
    }

    _createRoot(counterController) {
        const root = document.createElement("div");
        root.style.textAlign = "center";
        root.textContent = `${counterController.count}`;
        root.addEventListener("click", () => {
            counterController.increment();
            root.textContent = `${counterController.count}`;
        });
        return root;
    }

    getElement() {
        return this._element;
    }
}

