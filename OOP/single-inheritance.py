class Dog:

    def bark(self):
        print("The dog barks")

class Animal(Dog):
    def display(self):
        print("it is an animal class")



obj = Animal()

obj.bark()
obj.display()
