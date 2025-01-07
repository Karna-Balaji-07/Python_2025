# Anagrma

def anagram(s1,s2):
    for i in s1:
        if i not in s2:
            return False
    return True

def anagram2(s1,s2):
    n = len(s1)
    m = len(s2)
    s1 = sorted(s1)
    s2 = sorted(s2)
    index = 0
    if n > m:
        index = n
    else:
        index = m
    for i in range(index):
        if s1[i] != s2[i]:
            return False
    return True

s = "geeks"
a = "keegsabs"
print(anagram(s,a))
print(anagram2(s,a))
