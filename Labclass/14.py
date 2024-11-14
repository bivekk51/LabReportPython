class Employee:
    def get_salary(self,salary):
        self.salary=salary
        return self.salary
class Manager(Employee):
    def get_bonus(self,bonus):
        self.bonus=bonus
        return self.bonus+self.salary
employee1=Employee()
manager1=Manager()
print(f"Employee salary:{employee1.get_salary(5000)}")
print(f"Manager salary:{manager1.get_salary(8000)+manager1.get_bonus(6000)}")