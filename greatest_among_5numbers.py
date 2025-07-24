a = int ( input ( " enter the 1st number :"))

b = int ( input ( " enter the 2nd number :"))

c = int ( input ( " enter the 3rd number :"))

d = int ( input ( " enter the 4th number :"))

e = int ( input ( " enter the 5th number :"))

if ( a > b and  a > c and a >  d and a > e):
    print("the greatest number is ",a)
elif ( b > a and b > c and b > d and b > e):
    print('the greatest number is :',b)
elif (  c > a  and c > b and c > d and c > e):
    print('the greatest number is :',c)
elif (  d > a and d > b and d > c and d > e):
    print("the greastest number is :", d)
else:
    print('the greastest number is : ',e)
    