weight = int(input("Your weight: "))
conversion_type = input("L(lbs) or K(kilogram): ")
if conversion_type.lower() == "l":
    converted = weight * 0.45
    print(f"Your weight in {converted} kg")
else:
    converted = weight * 2.205
    print(f"Your weight in {converted} lbs")