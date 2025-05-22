# 345. Reverse Vowels of the String

def solution1(arr):
    first = 0
    last = len(arr)-1
    vowels = "AEIOUaeiou"
    s = []
    for i in arr:
        s.append(i)
    while first < last:
        if s[first] in vowels and s[last] in vowels:
            s[first],s[last] = s[last],s[first]
            first += 1
            last -= 1
        if s[first] not in vowels:
            first += 1
        if s[last] not in vowels:
            last -= 1
    return "".join(s)

s  = "IceCreAm"
s = "leetcode"
print(solution1(s))