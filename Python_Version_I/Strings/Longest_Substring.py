# Longest substring between any pair of occurrences ōf similar characters

def longest(s):
    n = len(s)
    res = 0
    diff = 0
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if s[i] == s[j]:
                diff = j-i-1
                res = max(res,diff)
    return res

s = "accabbacc"
print(longest(s))

