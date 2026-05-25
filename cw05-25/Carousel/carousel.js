// блок внутри которого будет хранится массив с элементами 
// которые можно по клику на правую и левую стрелочку менять

export class Carousel {
    /**
     * @param {HTMLElement} element
     * @param {Array<HTMLElement>} childrenElement
     */
    constructor(element, childrenElement) {
        this._element = element;
        this._childrenElement = childrenElement;
        this._rightBtn = document.createElement('button');
        this._leftBtn = document.createElement('button');
    }

    initialize() {

    }
}
