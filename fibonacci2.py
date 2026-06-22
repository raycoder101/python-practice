def fibonacci(n):
    if n <= 1:
        return n
    else:
        print("recursion ", n)
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(5))