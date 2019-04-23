#  https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 25, 57, 36]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_item_list = []
for item_1 in a:
    for item_2 in b:
        if item_2 == item_1 and item_2 not in common_item_list:
            common_item_list.append(item_1)
print(common_item_list)