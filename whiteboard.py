def powerOfTwo(n):
    if n==0:
        return 1
    else:
        power=powerOfTwo(n-1)
        power=power*2
        return power
        print(power)

print(powerOfTwo(5))
