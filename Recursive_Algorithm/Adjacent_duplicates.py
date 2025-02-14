# Adjacent duplicates

def recursion1(s):
    arr = ""
    n = len(s)
    i = 0
    while i < n:
        repeated = False
        while i+1 < n and s[i] == s[i+1]:
            repeated = True
            i += 1
        if not repeated:
            arr += s[i]
        i += 1
    if n == len(arr):
        return s
    return recursion1(arr)

print(recursion1("abbccbbaa"))

