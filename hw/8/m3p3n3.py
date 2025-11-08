count = 0
for num in range(100, 10000):
    digits = str(num)
    if len(digits) == len(set(digits)):
        count += 1
print(count)