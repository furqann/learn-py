# Common builtin functions
# int(), float(), str(), bool()
pounds = input("Your weight in pounds: ")  # Default is string. If you expecting any number, you must change it type.
print(type(pounds))
kilograms = float(pounds) / 2.205
print(type(kilograms))
print(kilograms)