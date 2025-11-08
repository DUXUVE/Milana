def temperature(temp):
    return -5 <= temp <= 25

def time(hour):
    return 7 <= hour <= 22

def can_go_outside(temp, current_hour):
    if temperature(temp) and time(current_hour):
        return "Можно идти гулять"
    else:
        return "Лучше остаться дома"

print(can_go_outside(20, 15)) 