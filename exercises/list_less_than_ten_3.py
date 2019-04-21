numbers_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

user_input = int(input("Enter your number to get list of numbers less than: "))
#  This method is know as list comprehension.
new_list = [num for num in numbers_list if num < user_input]
print([item for item in new_list])  # Printing in one line
