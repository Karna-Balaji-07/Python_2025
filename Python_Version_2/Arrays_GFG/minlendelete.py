
def solution1(s):
    left = 0
    right = len(s)-1
    while left <  right and s[left] == s[right]:
        char = s[left]
        while left < right and s[left] == char:
            left += 1
        while left <= right and s[right] == char:
            right  -= 1
        
    return right - left+1
            

    return len(s)
s = "cabaabac"
print(solution1(s))