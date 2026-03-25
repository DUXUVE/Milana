n = int(input("Число: "))
n1 = n % 10
n = n // 10
n2 = n % 10
n = n // 10
n3 = n % 10
n = n // 10
n4 = n % 10
p = n1 * n2 * n3 * n4
print(f"{p}")