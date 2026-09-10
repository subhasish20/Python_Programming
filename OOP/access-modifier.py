class BankAccount:

    def __init__(self, owner, password):
        # Public variable
        # Can be accessed directly from outside the class
        self.owner = owner

        # Protected variable
        # "_" means: "You should not access this directly"
        # But Python still allows you to access it
        self._branch = "Main Branch"

        # Private variable
        # "__" tells Python to use name mangling
        self.__password = password

    # Method inside the class
    def show_password(self):
        # We can access __password normally INSIDE the class
        print("Password:", self.__password)


# Create an object
account = BankAccount("Alice", "secret123")


# --------------------------------------------------
# 1. PUBLIC VARIABLE
# --------------------------------------------------

print(account.owner)

# Output:
# Alice

# Public variables can be accessed directly.


# --------------------------------------------------
# 2. PROTECTED VARIABLE
# --------------------------------------------------

print(account._branch)

# Output:
# Main Branch

# Python allows this, but "_" is a warning/convention:
# "This is intended for internal use."


# --------------------------------------------------
# 3. PRIVATE VARIABLE
# --------------------------------------------------

# This will NOT work:
#
# print(account.__password)
#
# Python will give:
# AttributeError
#
# Because Python changed the name internally.


# --------------------------------------------------
# 4. ACCESS PRIVATE VARIABLE USING A METHOD
# --------------------------------------------------

account.show_password()

# Output:
# Password: secret123

# This is the recommended way:
# The class itself provides a method to access the data.


# --------------------------------------------------
# 5. ACCESS PRIVATE VARIABLE USING NAME MANGLING
# --------------------------------------------------

print(account._BankAccount__password)

# Output:
# secret123

# Why does this work?
#
# Python internally changes:
#
#     __password
#
# into:
#
#     _BankAccount__password
#
# This is called NAME MANGLING.
#
# So __password is not truly private.
