a = int(input("Высота: "))
b = int(input("Ширина: "))
for row in range(a):
    for col in range(b):
        if (row == 0 or row == a - 1 or
            col == 0 or col == b - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()