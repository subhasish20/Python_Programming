x = int ( input('enter the range :'))
for i in range(1,x+1) :
    for j in range(x+1,i,-1) :
        print('*',end='')
    print()
