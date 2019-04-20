#  Exercise from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
from datetime import datetime as dt
name = input("Enter your name: ")
current_age = int(input("Enter your age: "))
total_copies = int(input("How many times you want to print: "))
present_year = dt.now().year
age_to_be = 100
hundred_year_in = (age_to_be - current_age) + present_year
print(f"You'll be 100 year old in {hundred_year_in}\n" * total_copies)
