class Product {
    constructor(name, price) {
        this.name = name;
        this.price = price; 
    }
}

class ShoppingCart {
    constructor(owner) {
        this.owner = owner;
        this.items = [];
    }

    addProduct(product) {
        this.items.push(product); [cite: 5]
    }

    getTotalPrice() {
        let total = 0; [cite: 7]
        for (let item of this.items) { [cite: 7, 8]
            total += item.price;
        }
        return total; [cite: 6]
    }
}

const apple = new Product("яблоко", 50);
const bread = new Product("хлеб", 40);
const milk = new Product("молоко", 80);
const myCart = new ShoppingCart("W");
myCart.addProduct(apple);
myCart.addProduct(bread);
myCart.addProduct(milk);

console.log(`итоговая сумма: ${myCart.getTotalPrice()}`); 