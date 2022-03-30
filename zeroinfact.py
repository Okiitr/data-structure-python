from math import floor
n = int(input('Enter a number of which you want factorial : '))
fct=1
for i in range (1,n+1):
    fct = fct*i
zeros=0
i=5
while i <=n :
    zeros=zeros+floor(n/i)
    i=i*5
    
print (f'factorial of {n}={fct}')
print (f'total zeros in {fct}={zeros}')
    