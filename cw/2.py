while True:
    n = int(input("Число: "))
    if n == 7:
        break
    elif n > 0:
        print("Positive")
    elif n == 0:
        print("Zero")
    else:
        print("Negative")
print("Good bye")
