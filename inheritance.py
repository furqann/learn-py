#  Inheritance
class Mammal:
    def walk(self):
        print("Walking started")


class Dog(Mammal):
    # Python does not allow empty classes we need to use a keyword pass
    def bark(self):
        print("Woof Woof")

    def walk(self):
        print("Dog walking")


class Cat(Mammal):
    def meow(self):
        print("Meow Meow")


dog = Dog()
dog.walk()