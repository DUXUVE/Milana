class Account {
    constructor(balance) {
        // this = {}
        this.balance = balance;
        // return this
    }

    withdraw(amount) {
        if (this.balance - amount >= 0) {
            this.balance -= amount;
            console.log(`снято ${amount}, баланс ${this.balance}`);
        }
        else {
            console.log("больше чем на балансе");
        }
    }

    deposit(amount) {
        this.balance += amount;
        console.log(`внесено ${amount}, баланс ${this.balance}`);
    }
}

const account = new Account(100);
account.withdraw(110);
console.log(account.balance);
account.withdraw(40);
account.deposit(50);