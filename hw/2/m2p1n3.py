m = int(input("Метры: "))
print("1.Мили\n2.Дюймы\n3.Ядры")
choice = int(input("Выбор: "))
if choice == 1:
    print (m * 1.6)
elif choice == 2:
    print (m * 39.37)
elif choice == 3:
    print (m * 0.9)