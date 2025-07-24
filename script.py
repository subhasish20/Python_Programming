
n=input('enter a number :')
if int(n)%10==0:
    print('can be divided by 10')
else:
    print('cannot be divided by 10 add ' + str(10-(int(n)%10)))
