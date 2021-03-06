#  Dictionary holds the key-value pairs and initial with {} brackets
customer = {
    "name": "John Reese",
    "age": 30,
    "verified": True
}
customer["name"] = "Jack Stefan"
print(customer["name"])
# print(customer["Name"]) #  This going throw exception.
print(customer.get("name"))  # Another way to get the value
print(customer.get("birthdate"))  # If key does not exist will return none
print(customer.get("Name", "No Name"))  # If key does not exist will return default set value

#  Exercise: Diplay 123 -> One Two Three
numbers = {
    "1":  "One",
    "2":  "Two",
    "3":  "Three",
    "4":  "Four"
}
phone_number = input("Any number: ")
output = ""
for digit in phone_number:
    output += numbers.get(digit, "!") + " "
print(output)