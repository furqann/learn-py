#  List
#  You can modify an item in a list using its index numbers[0] = 10
numbers = [1,2,300,4,5,10]
temp = 0
for number in numbers:
    if number > temp:
        temp = number
print(temp)

#  Some of the ways to show list
print(numbers[:])
print(numbers[-1])  # Display the last item in the list
print(numbers[2:4])  # Display the items from including index 2 upto 4 but excluding value of 4

#  2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

#  Exercise: Remove duplicates from a list
duplicate_list = [1,2,3,4,1,2]
unique_numbers = []
for number in duplicate_list:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)