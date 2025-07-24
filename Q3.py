#Program to swap two numbers

num1 = int ( input("enter the first number :"))

num2 = int ( input ("enter the second number :"))

print("before swap the numbers are :", num1 , "and", num2)

num1 , num2 = num2 , num1

print("after swap the numbers are :", num1 , "and", num2)
