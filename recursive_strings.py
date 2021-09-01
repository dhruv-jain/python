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
    
#returns trues if any of the array elements returns true when sent to callback functions
#example arr[2,4,6] false
#arr[8,9] true 9 is odd
def isOdd(num):
  if num%2==0:
       return False
   else:
       return True
        
def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True
