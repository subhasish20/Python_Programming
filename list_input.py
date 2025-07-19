#wirte a program to take input from user for making a list

L = []
n = int(input("enter how much number you want to add :"))
print("enter the element :")
for i in range(0,n):
    b = int(input())
    L.append(b)
print("elements are in the list :")
print(L)