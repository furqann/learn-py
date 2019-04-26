#  https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 25, 57, 36]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_without_duplicates = [item for item in set(a) & set(b)]

# One way not able to remove duplicates.
# common_item_list = [item for item in a if item in b]

# Common only and with duplicates removed.
# for item_1 in a:
#     for item_2 in b:
#         if item_2 == item_1 and item_2 not in common_item_list:
#             common_item_list.append(item_1)

print(common_without_duplicates)