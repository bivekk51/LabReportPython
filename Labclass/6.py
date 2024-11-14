class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
student1=Student("Alice","A")
print(f"Student Name:{student1.name}, Student Grade:{student1.grade}")