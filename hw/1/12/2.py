def calculate_room_area():
    length = float(input("Введите длину комнаты в метрах: "))
    width = float(input("Введите ширину комнаты в метрах: "))
    area = length * width
    print(f"Площадь комнаты: {area:.2f} м")

def convert_speed():
    kmh = float(input("Введите скорость в км/ч: "))
    ms = kmh * 1000 / 3600
    print(f"{kmh} км/ч = {ms:.2f} м/с")

def check_battery_life():
    current_charge = float(input("Введите текущий заряд в процентах: "))
    hours_left = float(input("Введите оставшееся время использования в часах: "))
    required_charge = hours_left * 12
    if current_charge >= required_charge:
        print("Хватит")
    else:
        print("Не хватит")

def main_menu():
    while True:
        print("1) Рассчитать площадь прямоугольной комнаты")
        print("2) Перевести скорость из км/ч в м/с")
        print("3) Узнать, хватит ли заряда телефона до конца дня")
        
        choice = input("Выбор: ")
        
        if choice == "1":
            calculate_room_area()
        elif choice == "2":
            convert_speed()
        elif choice == "3":
            check_battery_life()

if __name__ == "__main__":
    main_menu()