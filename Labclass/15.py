class BankAccount:
    def __init__(self,acc_holder,balance,acc_no):
        self.acc_holder=acc_holder
        self._balance=balance
        self.__acc_no=acc_no
    def show_details(self):
        print(f"Account holder:{self.acc_holder}")
        print(f"Balance:{self._balance}")
        print(f"Account number:{self.__acc_no}")
class Branch(BankAccount):
    def show(self):
        print(f"Account holder name:{self.acc_holder}")
        print(f"Total balance:{self._balance}")
account=BankAccount("Ankit",5000,9865452)
account.show_details()
branch1=Branch("Ankittt",8000,9956485)
branch1.show()
print(f"Public-Account holder:{account.acc_holder}")
print(f"Protected-Balance:{account._balance}")
print(f"Private-Account number:{account._BankAccount__acc_no}")
