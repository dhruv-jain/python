#Print reverse of a string 
def reverse(strng):
    if len(strng) == 1:
        return strng[0]
    return strng[-1] + reverse(strng[:-1])

#Return true if string is palindrome (same from start or end example - tacocat)
def isPalindrome(strng):
    if len(strng) == 1:
        return True
    if strng[0] == strng[-1]:
        return isPalindrome(strng[1:-1])
    return False
    
