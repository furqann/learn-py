"""
https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

"""
import random as r
a = r.sample(range(15),5)
b = r.sample(range(15),5)
print(f"Random generated lists\na: {a}\nb: {b}")
common = [n for n in (set(a) & set(b))]
print (f"Common: {common}")
