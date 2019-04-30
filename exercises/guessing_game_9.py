#  https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
import random as r
import math as m

random_num = m.ceil(r.random()*10)
total_try = 0

while True:
    user_guess = input("Your Guess: ")
    if user_guess == "exit":
        break
    total_try += 1
    user_guess = int(user_guess)
    if user_guess > random_num:
        print("Too high")
    elif user_guess < random_num:
        print("too low")
    else:
        print(f"Correct {user_guess} is equal to {random_num} in {total_try} tries")
        break

