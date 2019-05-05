#  https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
"""
Ask the user for a number and determine whether the number is prime or not.
"""
user_input = int(input("Enter number to check it is prime: "))
if user_input == 1:
    print("Not Prime")
elif user_input / user_input == 1:
    print("Prime")
