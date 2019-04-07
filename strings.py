lang = "python for experts"
lang_arr = lang[:]  # This will copy the whole string.
print(lang[:3])  # Left default value is 0
print(lang[0:3])  # Output will be pyt
print(lang[1:3])  # Output will be yt
#  What will be the output of lang[1:-1] ?
#  print(lang[1:-1])

#  Formatted String Literal
first_name = "Spencer"
last_name = "Reid"
message = f"{first_name} [{last_name}] is a investigator"
print(message)

#  Basic functions in python on strings
sentence = "Python for Beginners"
print(len(sentence))
print(sentence.title())  # Makes the first letter of each word capital.
print(sentence.upper())
print(sentence.lower())
print(sentence.find("or"))
print(sentence.replace("Beginners","Advance"))

#  Another way to find word in a string using in operator
print('Python' in sentence)  # Will return boolean value instead of index like using find method.