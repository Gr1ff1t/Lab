class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Example usage
student = Student("John", 20, "Example University")

print("Student's name:", student.name)
print("Student's age:", student.age)
print("Student's university:", student.university)

student.add_grade(85)
student.add_grade(90)
student.add_grade(78)

print("Student's grades:", student.grades)
print("Student's average grade:", student.average_grade())
