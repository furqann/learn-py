#  https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
#  http://www.asciitable.com/
"""
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
=> Extra:
  => Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
import random as r


def ran_gen():
  lower_alpha = chr(r.randint(97, 122))
  upper_alpha = chr(r.randint(69,78))
  special_char = chr(r.randint(33,47))
  numbers = str(r.randint(0,999))
  return lower_alpha + upper_alpha + special_char + numbers


password = ""
iterations = 5

while iterations > 0:
  password += ran_gen() 
  iterations -= 1

print(password)
