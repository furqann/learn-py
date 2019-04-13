#  Classes
class Person:
    def print_name(self):
        print("Some name")

    def print_address(self):
        print("Some address")


person1 = Person()  # Initialize
person1.name = "Reese"  # Property
person1.print_address()
print(person1.name)
