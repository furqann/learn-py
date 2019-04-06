# Common builtin functions
# int(), float(), str(), bool()
weight_lbs = input("Your weight in pounds: ")  # Default is string. If you expecting any number, you must change it type.
print(type(weight_lbs))  # Shows the type of the variable
weight_kg = float(weight_lbs) * 0.45
print(type(weight_kg))  # Shows the type of the variable
print(weight_kg)