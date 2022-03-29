from distutils.log import Log
from math import floor


n = int(input('Enter a number :'))
count=0

while n!=0:
    n=floor(n/10)
    count=count+1

print (f'Total digits in your number is :{count}')