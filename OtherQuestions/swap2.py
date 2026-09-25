a = int ( input ("enter the first number :"))
b = int ( input ("ente the second number :"))
print("before swapping a is :",a,end=' ')
print("before swapping b is :",b)
a += b
b = a - b
a = a - b
print("after swapping a is {}:".format(a),end='')
print("after swapping b is {}:".format(b),end='')


