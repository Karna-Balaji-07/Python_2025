# check if the string is palindrome using recursion

def solution1(left,right,s):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    solution1(left+1, right-1,s)