from random import randint
num_to_guess = randint(1, 500)
t = 0
while True:
    guess = int(input("Угадай число: "))
    if guess == 0:
        break
    t += 1
    if guess == num_to_guess:
        print("Да")
        break
    elif num_to_guess < guess:
        print("Меньше")
    else:
        print("Больше")