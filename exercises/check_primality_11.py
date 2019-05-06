#  https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
"""
Ask the user for a number and determine whether the number is prime or not.
"""


def is_prime(number):
    if number % 2 == 0:
        print("Prime")
    elif number % 3 == 0:
        print("Prime")
    elif number % 4 == 0:
        print("Prime")
    elif number % 5 == 0:
        print("Prime")
    elif number % 6 == 0:
        print("Prime")
    elif number % 8 == 0:
        print("Prime")
    elif number % 9 == 0:
        print("Prime")
    elif number % 10 == 0:
        print("Prime")
    else:
        print("Not Prime")


user_input = int(input("Enter number to check it is prime: "))
if user_input == 1:
    print("Not Prime")
else:
    is_prime(user_input)

