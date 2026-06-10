// блок внутри которого будет хранится массив с элементами 
// которые можно по клику на правую и левую стрелочку менять

export class Carousel { 
    /**
     * @param {HTMLElement} element
     * @param {Array<HTMLElement>} childrenElement
     */
    constructor(element, childrenElement, switchTimeout=null) {
        // Основной элемент-контейнер, в котором то что перематывать и кнопочки
        this._element = element;
        this._childElements = childrenElement;
        this._leftBtn = document.createElement('button');
        this._leftBtn.classList.add('left');
        this._leftBtn.classList.add('carousel__button');
        this._leftBtn.textContent = '<';
        this._rightBtn.classList.add('right');
        this._rightBtn = document.createElement('button');
        this._rightBtn.classList.add('carousel__button');
        this._rightBtn.textContent = '>';
        const carouselInner = document.querySelector(".carousel-inner");
        this._index = 0;
        this._leftBtn.addEventListener('click', () => {
            if (this._setInterval) { clearInterval(this._setInterval); }
            this._index = this._index === 0 ? this._childElements.length - 1 : this._index - 1;
            carouselInner.style.left = `-${this._index * 100}%`;
        });
        this._rightBtn.addEventListener('click', () => {
            if (this._setInterval) { clearInterval(this._setInterval); }
            this._index = this._index === this._childElements.length - 1 ? 0 : this._index + 1;
            carouselInner.style.left = `-${this._index * 100}%`;
        });

        this._element.append(this._leftBtn, this._rightBtn);

        if (switchTimeout != null) {
            this._setInterval = setInterval(() => {
                this._index = this._index === 0 ? this._childElements.length - 1 : this._index - 1;
                carouselInner.style.left = `-${this._index * 100}%`;
            }, switchTimeout);
        } 
    }

    
}
