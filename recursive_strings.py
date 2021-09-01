def reverse(strng):
    if len(strng) == 1:
        return strng[0]
    return strng[-1] + reverse(strng[:-1])
