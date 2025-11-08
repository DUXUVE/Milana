while True:
    usd = 0.012
    cny = 0.088
    s = int(input("Рубли: "))
    print("1.Доллоры \n2.Юани")
    choise = input("")
    if choise == "1":
        print(s * usd)
    elif choise == "2":
        print(s * cny)
    print("Продолжить?")
    if input().strip().lower() != "да":
        break
