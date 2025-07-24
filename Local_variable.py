#whenever a variable is defined in a function , it is can be use only in that function.The variable can not  be accessed from the outside of the function. 

# local scope of variables is given below

def demo():
    a  = 100
    print(a)
    
    #in this case "a" is a  local variable because it is inside a  fumctiom  or  declare under a function
#calling the functiom
demo()
#if we will declare this function outside of the function then it woll not execute