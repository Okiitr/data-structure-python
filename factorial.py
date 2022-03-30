def factorial(n):
    if n ==0 or n == 1:
        return 1
    else:
        fct = n * factorial(n-1)
        return fct
    
n = int(input('Enter a number of which you want factorial : '))
print(f'Factorial of {n} = {factorial(n)}')