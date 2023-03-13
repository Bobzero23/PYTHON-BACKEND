# creating a class
class MyClass:
    x = 5


# creating object
object = MyClass()

# calling object
print(object.x)


# this like constructor in other languages
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


personObject = Person("Bobzero", 23)

print(personObject.name)
