#  Exercise from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
total_copies = int(input("How many times you want to print: "))
year = datetime.datetime.now()
hundred_year = (100 - age) + year.year
print(f"You'll be 100 year old in {hundred_year}\n" * total_copies)
