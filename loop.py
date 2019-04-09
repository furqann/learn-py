#  Basic for loop
for item in 'Python':
    print(item)
for item in ['John','Ali','Sana']:
    print(item)
for item in [0, 20]:
    print(item)

#  Range function in loop
for item in range(5):
    print(item)
for item in range(10,15):
    print(item)
for item in range(20,30,2):
    print(item)

#  Exercise
#  Print the total cost of items in a list
itemList = [10, 20, 30]
totalCost = 0
for item in itemList:
    totalCost += item
print(f"Total cost: {totalCost}")