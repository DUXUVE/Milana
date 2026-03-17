// 1 
// Базовый класс маркера
class Marker {
    constructor(color, inkLevel) {
        this.color = color;
        this.inkLevel = inkLevel;
    }
    
    print(text) {
        let printedText = "";
        let ink = this.inkLevel;
        
        for (let i = 0; i < text.length; i++) {
            if (text[i] !== " ") {
                if (ink >= 0.5) {
                    printedText += text[i];
                    ink -= 0.5;
                } else {
                    break;
                }
            } else {
                printedText += " ";
            }
        }
        
        console.log("%c" + printedText, "color: " + this.color);
        this.inkLevel = ink;
    }
}

class RefillableMarker extends Marker {
    constructor(color, inkLevel) {
        super(color, inkLevel);
    }
    
    refill() {
        this.inkLevel = 100;
        console.log("маркер заправлен до 100%");
    }
}

let marker = new RefillableMarker("blue", 10);
marker.print("sjdkfskhgfkxhdgkhxkjhgkjhbn");
console.log("осталось чернил: " + marker.inkLevel);



// 2
class ExtendedDate extends Date {
    constructor(...args) {
        super(...args);
    }
    
    getDateText() {
        const months = [
            "января", "февраля", "марта", "апреля", "мая", "июня",
            "июля", "августа", "сентября", "октября", "ноября", "декабря"
        ];
        
        return this.getDate() + " " + months[this.getMonth()];
    }
    
    isFutureOrPresent() {
        let now = new Date();
        return this >= now;
    }
    
    isLeapYear() {
        let year = this.getFullYear();
        return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
    }
    
    getNextDate() {
        let next = new ExtendedDate(this);
        next.setDate(this.getDate() + 1);
        return next;
    }
}

let date1 = new ExtendedDate(2025, 2, 15); 
console.log(date1.getDateText());
console.log(date1.isFutureOrPresent());
console.log(date1.isLeapYear());
console.log(date1.getNextDate().toDateString());