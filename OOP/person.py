class Person:
    def __init__(self, name,age, num):
        self.name = name
        self.age = age
        self.num = num
        print(f"Name: {self.name}, Age: {self.age}, Num: {self.num}")
    
person1 = Person("Alice", 30, 12345)
person1.name = "Bob"
print(person1.name)
