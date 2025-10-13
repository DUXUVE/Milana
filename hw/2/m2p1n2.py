n1 = int(input("Первое число: "))
n2 = int(input("Второе число: "))
n3 = int(input("Третее число: "))
print("1.Минимум\n2.Максимум\n3.Среднее арифметическое")
choice = int(input("Выбор: "))
if choice == 1 and n1 < n2 and n1 < n3:
    print (n1)
elif choice == 1 and n2 < n1 and n2 < n3:
    print (n2)
elif choice == 1 and n3 < n2 and n3 < n1:
    print (n2)
elif choice == 2 and n1 > n2 and n1 > n3:
    print (n1)
elif choice == 2 and n2 > n1 and n2 > n3:
    print (n2)
elif choice == 2 and n3 > n2 and n3 > n1:
    print (n3)
elif choice == 3:
    print (n1 + n2 + n3 / 3)
