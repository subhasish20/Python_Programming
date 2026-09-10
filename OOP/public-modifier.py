class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)


s1 = Student("Rahul", 20)

# Accessing public variables
print(s1.name)
print(s1.age)

# Changing values
s1.name = "Amit"
s1.age = 21

print(s1.name)
print(s1.age)

# Calling public method
s1.display()
