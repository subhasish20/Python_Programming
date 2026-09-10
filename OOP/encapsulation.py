class BankAccount:

    def __init__(self, owner, balance):
        # Public variable
        self.owner = owner

        # "Private" variable
        # We don't want outside code to directly change it
        self.__balance = balance

    # Method to check the balance
    def get_balance(self):
        return self.__balance

    # Method to deposit money
    def deposit(self, amount):

        # Check if the amount is valid
        if amount > 0:
            self.__balance += amount
            print("Money deposited successfully!")
        else:
            print("Invalid amount!")


# Create an account
account = BankAccount("Alice", 1000)


# We can access the public variable
print(account.owner)
# Output: Alice


# We should NOT directly access __balance
# print(account.__balance)
# This gives an AttributeError


# Instead, use the method provided by the class
print(account.get_balance())
# Output: 1000


# Deposit money using the method
account.deposit(500)

print(account.get_balance())
# Output: 1500
