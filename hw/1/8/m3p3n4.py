num = input("Введите число: ")
result = ''
for digit in num:
    if digit != '3' and digit != '6':
        result += digit
print(result)