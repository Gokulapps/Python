class bank:
    def __init__(self,account_no,account_balance,transaction_type,amount):
        self.__account_no=account_no
        self.__account_balance=account_balance
        self.transaction_type=transaction_type
        self.__amount=amount
    def calculate_balance(self):
        if(self.transaction_type=="withdrawal"):
            self.__account_balance=self.__account_balance-self.__amount
            return self.__account_balance
        elif(self.transaction_type=="debit"):
            self.__account_balance=self.__account_balance+self.__amount
            return self.__account_balance
        elif(self.transaction_type=="check balance"):
            return self.__account_balance
    def get_account_balance(self):
        return self.__account_balance

a=bank(111223,100000,"withdrawal",1000)
print(a.calculate_balance())
b=bank(112232,10000000,"debit",10000)
print(b.calculate_balance())
            
            
