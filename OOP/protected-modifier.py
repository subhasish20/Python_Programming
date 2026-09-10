class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    def display(self):
        print(self.name)
        print(self._marks)


s1 = Student("Rahul", 90)

print(s1.name)
print(s1._marks)
