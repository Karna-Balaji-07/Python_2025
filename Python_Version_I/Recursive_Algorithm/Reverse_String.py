# Reverse a string

def reverse1(s):
    return s[::-1]

def reverse2(s):
    if len(s) == 0:
        return s
    return reverse1(s[1:]) + s[0]

def reverse3(s,n):
    if n == 1:
        return s[0]
    return s[n-1] + reverse3(s,n-1)

s = "Helllo world"
print(reverse3(s, len(s)))

