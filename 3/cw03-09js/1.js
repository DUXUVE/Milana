// function PhoneData (model, memory) {
//     this.model = model;
//     this.memory = memory;
//     this.batteryCharge = 0;
// }

// const phone = new PhoneData("dgs", 200);
// console.log(phone);

function Pet (name, type) {
    this.name = name;
    this.type = type;
}
Pet.prototype.getInfo = function () {
    // this = p
    console.log(this.name, this.type);
};

const p = new Pet('a', 'b')
p.getInfo()