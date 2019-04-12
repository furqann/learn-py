#  Exceptions handling
#  Always look at the Process finished with exit code 0/1 if its 0 means success else 1 means crashed
try:
    age = int(input("Age > "))
    output = 2000/age
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid age")
