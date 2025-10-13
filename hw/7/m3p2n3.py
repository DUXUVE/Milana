while True:
    num = int(input())
    if num == 7:
        print("Good bye!")
        break
    if num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")