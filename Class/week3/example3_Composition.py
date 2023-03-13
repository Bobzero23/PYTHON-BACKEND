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
object.add(Student("Bobzero", "NoName"))
object.add(Student("TheProblem", "NoName"))

for student in object.sutdents:
    print(student.firstName, " ", student.lastName)
