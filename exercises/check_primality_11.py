#  https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
"""
Ask the user for a number and determine whether the number is prime or not.
"""
user_input = int(input("Enter number to check it is prime: "))

if user_input <= 0:
    print("Invalid input")
elif user_input == 1:
    print("Not Prime")
else:
    divided_by = [num for num in range(2, user_input+1) if user_input % num == 0]
    if len(divided_by) > 1:
        print("Not prime")
    else:
        print("Prime")

