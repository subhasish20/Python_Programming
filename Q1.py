#Write a program to find oldest among three age.

age1 = int ( input ("enter the first age of the 1st man :"))

age2 = int ( input ("enter the second age of the 2nd man :"))

age3 = int ( input ("enter the third age of the 3rd man :"))

if age1 > age2 and age1 > age3:
    print("the greatest age is",age1,"of ag1 man")
elif age2 > age3 :
    print("the greatest age is",age2,"of ag2 man")
else:
    print("the greatest age is",age3,"of ag3 man")