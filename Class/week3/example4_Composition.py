class Department:
    def __init__(self):
        self.sutdents = []

    def add(self, student):
        self.sutdents.append(student)


class Student:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


object = Department()

for i in range(5):
    firstName = str(input("Enter firstName: "))
    lastName = str(input("Enter lastName: "))
    object.add(Student(firstName, lastName))

for student in object.sutdents:
    print(student.firstName, " ", student.lastName)
