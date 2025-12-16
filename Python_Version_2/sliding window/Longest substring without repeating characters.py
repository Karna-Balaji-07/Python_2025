# Find the longest substring without repeating characters

def solution(s):
    n = len(s)
    left = 0
    right = 0
    result = 0
    sets = set()
    while right < n:
        if s[right] in sets:
            while s[right] in sets:
                sets.remove(s[left])
                left += 1
        sets.add(s[right])
        result = max(result, right - left + 1)
        right += 1

    return result

s = "abcdefabcbb"
print(solution(s))