class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
    
    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False
       
    def display_balance(self):
        print (f"Current Balance: ${self._balance:.2f}")
    
    
         
    
    

        
