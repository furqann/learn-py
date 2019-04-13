#  Classes
class Person:
    def __init__(self, name):  # Constructor
        self.name = name

    def print_name(self):
        print(self.name)

    def print_address(self):
        print("Some address")


person1 = Person("John")  # Initialize
# person1.name = "Reese"  # Property
person1.print_name()
print(person1.name)
