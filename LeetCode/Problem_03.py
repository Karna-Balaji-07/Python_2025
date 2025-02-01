# Longest Substring Without Repeating Characters

def substring(s):
    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 2
    result = 0
    for i in range(n):
        for j in range(i+1,n+1):
            if len(set(s[i:j])) == len(s[i:j]):
                result = max(result, j-i)
    return result

def substring1(s):
    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 2
    result = 0
    dicts = {}
    left = 0
    for right in range(n):
        if s[right] in dicts:
            left = max(dicts[s[right]], left)
        result = max(result, right - left + 1)
        dicts[s[right]] = right + 1
    return result

s = "bbbbb"
print(substring1(s))