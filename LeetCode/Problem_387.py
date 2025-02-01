# First unique character in a string

def unique(s):
    n = len(s)
    dicts= {}
    for i in s:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1
    for i in range(n):
        if dicts[s[i]] == 1:
            return i
    return  -1

s = "leetcode"
print(unique(s))