#A variable has a  global scope , if it's created outside the function i.e. the code body are accessible from anywhere

#An example of globa variable is given below......

a = 1000
#here "a" is a global variable

def demo():
    print(a)
    #under a fumction the value will execute
    
print(a)
#here also the value will execute

demo()

'''we can change the value of the global variable by using global keyword
   the syntax is : global variable___name'''
'''now we are changing the value of the global variable'''

def new():
    global a
    #by writting "global 10" the  value of the a will change from here according to given rule  
    a = 50
    print(a)

new()

print(a)