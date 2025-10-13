n1 = int(input("Первое число: "))
n2 = int(input("Второе число: "))
n3 = int(input("Третее число: "))
print("1.Сумма\n2.Произведение")
choice = input("Выбор: ")
if choice == ("1"):
    print(f"{n1 + n2 + n3}")
if choice == ("2"):
    print(f"{n1 * n2 * n3}")