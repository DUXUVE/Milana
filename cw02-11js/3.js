function min (number1, number2) {
    if (number1 == null || number2 == null) {
        throw new Error("Нельзя сравнить null с number");

    }
    if (number1 <= number2) {

        return number1;
      
    }
    
     else {
        return number2;
     }
}

function testMin() {
    console.log(min(3, 5) === 3);
    console.log(min(5, 3) === 3);
    console.log(min(3, 3) === 3);
    try {
        min(null,3);
        min(3,null);
        console.log(false);
    } catch { 
        console.log(true);
    }
}
