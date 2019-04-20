import datetime
name = input("Enter your name: ")
age  = int(input("Enter your age: "))
year = datetime.datetime.now()
hundred_year = (100 - age) + year.year
print(f"You'll be 100 year old in {hundred_year}")
