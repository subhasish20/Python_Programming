class Main:
    name = "Subhasish Jena"

    def __init__(self,age:int) -> None:
        self.age = age



obj = Main(5)

print(Main.name,"age is ", obj.age)


###############  example 2 ####################

class Student:
    school_name = "Global High"  # This is a class variable

    def __init__(self, name):
        self.name = name         # This is an instance variable

# Create two different students
student1 = Student("Alice")
student2 = Student("Bob")

# Both have different names, but share the same school
print(student1.name + " goes to " + Student.school_name)
print(student2.name + " goes to " + Student.school_name)
