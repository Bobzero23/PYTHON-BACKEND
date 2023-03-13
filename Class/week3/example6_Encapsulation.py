class Student:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def getName(self):
        return self.firstName


object = Student("Bob", "zero", 88)
print(object.getName())
