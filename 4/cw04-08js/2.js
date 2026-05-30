class Player {
    constructor(name, health) {
        this.name = name;
        this.health = health;
        this.weapon = null;
    }
    equip(weapon) {
        this.weapon = weapon;
    }
    attack(player) {
        player.health -= this.weapon.damage;
        if (!this.weapon) {
            console.log("атака невозможна");
        }
    }
}

class Weapon {
    constructor(name, damage) {
        this.name = name;
        this.damage = damage;
    }
}

const player1 = new Player("Aaa", 100);
const player2 = new Player("Bbb", 100);
const sword = new Weapon("Sword", 10);

player.equip(sword);
player1.attack(player2);
console.log();