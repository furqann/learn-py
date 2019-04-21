numbers_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_input = int(input("Enter your number to get list of numbers less than: "))
new_list = []
for num in numbers_list:
    if num < user_input:
        new_list.append(num)

for num in new_list:
    print(num)
