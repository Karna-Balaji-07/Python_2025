# Palindrome.py

def palindrome1(s):
    return s == s[::-1]

def palindrome2(s):
    string = "".join(reversed(s))
    return string == s

def palindrome3(s):
    left = 0
    right = len(s) - 1
    while right >= left:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


s ="ababa"
print(palindrome1(s))
print(palindrome2(s))
print(palindrome3(s))