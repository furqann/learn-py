#  Classes
class Person:
    def __init__(self, name):  # Constructor
        self.name = name

    def talk(self):
        print(f"My name is {self.name}")


person1 = Person("Ali")  # Initialize
# person1.name = "Reese"  # Property
person1.talk()
