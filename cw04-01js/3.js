class Cowboy {
    constructor(name, health, damage) {
        this.name = name;
        this.health = health;
        this.damage = damage;
    }

    shoot(cowboy) {
        cowboy.health -= cowboy.damage
    }
}

const cowboy1 = new Cowboy("A", 100, 10);
const cowboy2 = new Cowboy("B", 100, 8);

cowboy1.shoot(cowboy2);
