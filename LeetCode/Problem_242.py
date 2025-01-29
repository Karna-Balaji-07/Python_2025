# Valid anagram

def anagram1(s1,s2):
    s1=  "".join(sorted(s1))
    s2="".join(sorted(s2))
    return s1==s2

def anagram2(s1,s2):
    if len(s1) != len(s2):
        return False
    for i in set(s1):
        if s1.count(i) != s2.count(i):
            return False
    return True

s = "anagram"
t = "nagaram"
print(anagram1(s,t))
print(anagram2(s,t))