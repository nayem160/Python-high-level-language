class Student:
    def __init__(self, name, age, grade, id):
        self.name = name
        self.age = age
        self.grade = grade
        self.id = id

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}\nID: {self.id}")


student1 = Student("John Doe", 20, "A", "12345")
student1.display()
