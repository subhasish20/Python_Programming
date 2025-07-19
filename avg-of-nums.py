a = int ( input ("enter the number to get the avg of the series :")) #user input

i = 0
sum = 0
while ( i <= a) :
    sum = sum + i
    i = i + 1 #increment
    
avg = float(sum) / 10
print("the avg of the series is :",avg)