class Person:
    def __init__(self,name=None,age=None):
        self._name=name
        self._age=age
    
    def set_name(self,name):
        self._name=name
    
    def get_name(self):
        return self._name
    
    def set_age(self,age):
        self._age=age
    
    def get_age(self):
        return self._age
person=Person()
person.set_name("john")
person.set_age(30)

print("Name:",person.get_name())
print("Age:",person.get_age())