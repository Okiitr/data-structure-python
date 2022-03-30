n = int (input ('Enter a number :'))

x=True
for i in range(2,n):
    if n%i == 0:
        x=False
        break
   
if x :
    print(f'Your number {n} is a Prime number')
else:
    print(f'Your number {n} is a Non-Prime number')
