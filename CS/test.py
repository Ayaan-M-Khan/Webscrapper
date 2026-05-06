class BankAccount:
    def __init__(self, balance, name):
        self.__balance = balance
        self.name = name
    
    def balance(self):
            return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            return False
        
# Test cases
if __name__ == "__main__":
    account = BankAccount(0, "Ayaan")
    print("Initial balance:", account.balance())  # Expected: 0

    account.deposit(100)
    print("Balance after deposit of $100:", account.balance())  # Expected: 100

    success = account.withdraw(30)
    print("Withdrawal of $30 successful?", success)  # Expected: True
    print("Balance after withdrawal of $30:", account.balance())  # Expected: 70

    success = account.withdraw(80)
    print("Withdrawal of $80 successful?", success)  # Expected: False
    print("Balance after attempted withdrawal of $80:", account.balance())  # Expected: 70

    for i in range(1,5):
        print (f"Balance after deposit of ${i*10}:", end=" ")
        account.deposit(i*10)