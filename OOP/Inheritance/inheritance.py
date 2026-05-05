class Person:
    def __init__(self, name,age, num):
        self.name = name
        self.age = age
        self.num = num




class Student(Person):
    def __init__(self,name,age,num,grade,id):
        super().__init__(name,age,num)
        self.grade=grade
        self.id=id
    
    def display(self):
         print(f"Name: {self.name}, Age: {self.age}, Num: {self.num}, Grade: {self.grade}, ID: {self.id} ")
    
S1=Student("Nayem", 23, "01516540037", 3.71, 160)

S1.display()
