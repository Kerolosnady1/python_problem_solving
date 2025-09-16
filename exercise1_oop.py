

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Hello, {self.name}. Your age is {self.age}"
    

person_info = Student("Kerolos", 20)

print(person_info)