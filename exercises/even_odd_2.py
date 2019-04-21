#  Basic task
def is_number_even_or_odd(number):
    return number % 2 == 0;


number = int(input("Enter the number: "))
if number % 4 == 0:
    print("Number is multiple of 4")
elif is_number_even_or_odd(number):
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")
