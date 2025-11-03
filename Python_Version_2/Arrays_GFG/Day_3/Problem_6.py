# 680. valid palindrome II

def solution1(s):
    arr = ""
    for i in range(len(s)):
        arr = ""
        arr = s[:i] + s[i+1:]
        if arr == arr[::-1]:
            return True
    return False

def solution2(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] != arr[right]:
            return palindrome(left+1,right,arr) or palindrome(left,right-1,arr)
        left += 1
        right -= 1
    return True


def palindrome(left,right,s):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True





s  = "abcaaa"
print(solution2(s))