a = int(input("Высота: "))
b = int(input("Ширина: "))
for row in range(a):
    for col in range(b):
        print("*", end="")
    print()