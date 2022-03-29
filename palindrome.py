from math import floor
n = int(input('Enter a positive number :'))
count=0
n1=n
n3=n
while n!=0:
    n=floor(n/10)
    count=count+1
    
n2=0
i=0
for i in range(count):
    a = n1%10
    n2=(n2*10)+a
    n1=int((n1-a)/10)
  
  
if n3==n2:
    print('palindrome')
    
else:
    print('not a plindrome')




