total = 0
maximum = float('-inf')
minimum = float('inf')

while True:
    num = int(input())
    if num == 7:
        print("Good bye!")
        break
    total += num
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Сумма:", total)
print("Максимум:", maximum)
print("Минимум:", minimum)