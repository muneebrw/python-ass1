def factorial(n):
    
    factorial = 1
    if n >= 1:
        for i in range (1,n+1):
            factorial = factorial * i
        print("Factorail of ",n , " is : ",factorial)

factorial(7)