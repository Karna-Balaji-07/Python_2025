# Problem - 09 => Palindrome Number

def palindrome(x):
    x = str(x)
    s = x[::-1]
    if s == x:
        return True
    else:
        return False
    

x = -121
print(palindrome(x))
