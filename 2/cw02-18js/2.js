
function getDaysCount(month, year) {
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

function isLeap(year) {
    return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
}

function countLeapYears(year) {
    let count = 0;
    for (let i = 4; i < year; i += 4) {
        if (isLeap(i)) {
            count++;
        }
    }
    return count;
}