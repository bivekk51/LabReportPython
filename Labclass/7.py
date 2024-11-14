class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def update_grade(self,new_grade):
        self.new_grade=new_grade
        print(f"{self.name}'s grade has been updated to {self.grade}")
student1=Student("Alice","B")
print(f"{student1.name}'s grade is {student1.grade}")
student1.update_grade("A")
print(f"{student1.name}'s has been updated to {student1.new_grade}")