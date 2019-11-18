def factorial(n):
    return 1 if(n==1 or n==0) else n * factorial (n-1);

print("Enter any number to get its factorial")
x =int(input())
print("factorial of ",x," is ",factorial(x))
