class BankAccount:
    def __init__(self,):
        self._balance = 0
    
    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False
       
    def display_balance(self):
        print (f"your current balance is: {self._balance}")
        pass
    
         
    
    

        
