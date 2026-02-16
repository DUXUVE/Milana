function isLeap(year) {
    return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
}
function getDaysCount(month) {
    switch(month) {
        case 2:
            return isLeap(year) ? 29 : 28;
        case 4:
        case 6:
        case 9:
        case 11:
            return 30;
        default:
            return 31;
    }
}
function getNextDayFormated(day, month, year) {
    const monthsPerYear = 12;
    day++;
    if (day > getDaysCount(month)) {
        day = 1;
        month++;
    }
    if (month > monthsPerYear) {
        year++;
        month = 1;
    }
    const dayFormated = String(day).padStart(2, '0');
    const monthFormated = String(month).padStart(2, '0');
    const yearFormated = String(year).padStart(4, '0');
    return `${dayFormated}.${monthFormated}.${yearFormated}`;
}
function testGetDaysCount() {
    console.log(getDaysCount(1, 2000) == 31);
    console.log(getDaysCount(2, 2000) == 29);
    console.log(getDaysCount(2, 2001) == 28);
    console.log(getDaysCount(3, 2000) == 31);
    console.log(getDaysCount(4, 2000) == 30);
    console.log(getDaysCount(5, 2000) == 31);
    console.log(getDaysCount(6, 2000) == 30);
    console.log(getDaysCount(7, 2000) == 31);
    console.log(getDaysCount(8, 2000) == 31);
    console.log(getDaysCount(9, 2000) == 30);
    console.log(getDaysCount(10, 2000) == 31);
    console.log(getDaysCount(11, 2000) == 30);
    console.log(getDaysCount(12, 2000) == 31);
    console.log();
}
function testNextDayFormated() {
    console.log(getNextDayFormated(6, 6, 2000) == "07.06.2000")
    console.log(getNextDayFormated(30, 6, 2000) == "01.07.2000")
    console.log(getNextDayFormated(31, 5, 2000) == "01.06.2000")
    console.log(getNextDayFormated(29, 2, 2000) == "01.03.2000")
    console.log(getNextDayFormated(28, 2, 2000) == "29.02.2000")
}