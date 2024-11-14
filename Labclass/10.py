class Parent:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
class Child(Parent):
    def add(self):
        return self.num1+self.num2
child1=Child(2,3)
print(f"The sum is: {child1.add()}")