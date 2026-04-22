import { CardElement } from "./Card";

export class GameContainer {
    constructor(element, rows, cols) {
        this._maxOpenedCount = 2;
        this._element = element;
        if (rows * cols % this._maxOpenedCount != 0) {
            throw new Error("Game can't have odd amount of cards");
        }
        this._rows = rows;
        this._cols = cols;
        this._cardElements = this.ganerateCards();
        this._openedCards = [];
    }

    initialize() {
        this._cardElements.forEach((card) =>
            this._element.appendChild(card.getElement()),
        );
    }

    addCardClickListener() {
        this._element.addEventListener('click', (event) => {
            const cardHTMLElement = event.target.closest(CardElement.className);
            if (!cardHTMLElement) {
                return;
            }
            
            const selectCard = this._cardElements.find(
                (cardElement) => cardElement.getElement() == cardHTMLElement,
            );

            if (selectCard.guessed) return;

            selectCard.show();

            if (this._openedCards.length >= this._maxOpenedCount) {
                this._openedCards.forEach(card => card.hide());
                this._openedCards = [];
            }

            this._openedCards.push(selectCard);
        });
    }

    getElement() {
        return this._element;
    }

    ganerateCards() {
        const pairsCount = this._rows * this._cols / 2;

        const [hiddenColor, ...cardColors] = this._generatepalette(pairsCount + 1)

        const cardElements = [];
        for (let i = 0; i < pairsCount; i++) {
            const card = new CardElement(document.createElement('li'));
            cardElements.push(card);
            cardElements.push(card.clone());
        }

        cardElements.sort(() => Math.random() - 0.5);
        return cardElements;
    }
}