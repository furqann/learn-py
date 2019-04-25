#  https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
#  Whether the input string is palindrome


def is_palindrome(word):
    to_string = str(word)
    reverse = to_string[::-1]
    return reverse == to_string


user_input = input("Enter a palindrome: ")
print(is_palindrome(user_input))
