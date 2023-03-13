class Department:
    def __init__(self):
        self.sutdents = []

    def add(self, student):
        self.sutdents.append(student)


class Student:
    def __init__(self, firstName, lastName, birthYear):
        self.firstName = firstName
        self.lastName = lastName
        self.birthYear = birthYear


object = Department()

for i in range(5):
    firstName = str(input("Enter firstName: "))
    lastName = str(input("Enter lastName: "))
    birthYear = int(input("Enter birthYear: "))
    object.add(Student(firstName, lastName))

for student in object.sutdents:
    if (2023 - student.birthYear) > 20:
        print(student.firstName, " ", student.lastName, " ", student.birthYear)
