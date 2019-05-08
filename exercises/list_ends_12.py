#  https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
"""
Write a program that takes a list of numbers (e.g, a = [5, 10, 15, 20, 25]) and 
makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
"""
def get_first_last_item(list_num):
  if len(list_num) == 0:
    return []
  elif len(list_num) == 1:
    return list_num
  elif len(list_num) >= 1:
    return [list_num[0],list_num[-1]]

print(get_first_last_item([1,2,34,5,7]))
print(get_first_last_item([]))
print(get_first_last_item([2,3]))
