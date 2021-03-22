def factorial(n):
    assert n>=0 and int(n) == n, "input can only be integers"

    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(102))