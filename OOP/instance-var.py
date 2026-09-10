class Student:
    def set_name(self, name):
        self.name = name  # This is an instance variable

student1 = Student()
student2 = Student()

student1.set_name("Alice")
student2.set_name("Bob")

print(student1.name)
print(student2.name)
