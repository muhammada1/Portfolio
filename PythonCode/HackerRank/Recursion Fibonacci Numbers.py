def fibonacci(n):
    if n<=1:
        return n
    else:
        n = fibonacci(n-1) + fibonacci(n-2)
        return n    

n = int(input())
print(fibonacci(n))
