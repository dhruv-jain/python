# Factorial of a number using recursion
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


def powerOfTwo(n):
    if n==0:
        return 1
    else:
        power=powerOfTwo(n-1)
        power=power*2
        return power
        print(power)

print(powerOfTwo(5))


#product of Array - productOfArray([1,2,3]) #6
def productOfArray(arr):
    res = 1
    
    for i in arr:
        res = res * i
    return res
