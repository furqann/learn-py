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