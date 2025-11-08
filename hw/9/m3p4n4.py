length = int(input("Введите длину: "))
width = int(input("Введите ширину: "))
for i in range(width):
    if i == 0 or i == width - 1:
        print('*' * length)
    else:
        print('*' + ' ' * (length - 2) + '*')