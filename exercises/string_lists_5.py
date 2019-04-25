#  https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
#  Whether the input string is palindrome


def is_palindrome(word):
    reverse = word[::-1]
    return reverse == word


user_input = str(input("Enter a palindrome: "))
print(is_palindrome(user_input))
