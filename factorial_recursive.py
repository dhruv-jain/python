def factorial(n):
    assert n>=0 and int(n) == n, "input can only be integers"

    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(102))

def sumofDigits(n):
    assert n>=0 and int(n) == n, 'The number has to be positive integer only'
    if n ==0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))

print(sumofDigits(-23))

# created by Dhruv Jain on March 27th 2021

def fibonacci(n):
    assert n>=0 and int(n) == n, "Fibonacci cannot be negative or non integer"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(-7))

