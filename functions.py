#  Different types of functions
def greet_user(first_name, last_name):
    print(f"Hi, {first_name} {last_name}")
    print("Welcome aboard")


greet_user("John", "Shawn")  # Positional arguments
greet_user(last_name="John", first_name="Shawn")  # Keyword arguments

#  Return function
#  All functions in python returns the value None

def square(number):
    return number*number


print(square(2))