# created by Dhruv Jain on March 27th 2021

def fibonacci(n):
    assert n>=0 and int(n) == n, "Fibonacci cannot be negative or non integer"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(-7))