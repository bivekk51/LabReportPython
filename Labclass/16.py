class ComplexNumber:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def __add__(self, other):
        return ComplexNumber(self.num1+other.num1, self.num2+other.num2)
    def __str__(self):
        return f"{self.num1}+{self.num2}i"
num5=ComplexNumber(2,3)
num6=ComplexNumber(5,6)
result=num5+num6
print(f"Sum of number:{result}")