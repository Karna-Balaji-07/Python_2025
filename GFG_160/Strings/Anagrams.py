# Anagrams 

def anagrams(s1,s2):
    dicts= {}
    for i in s1:
        dicts[i] = dicts.get(i,0)+1
    for i in s2:
        dicts[i] = dicts.get(i,0)-1
    for value in dicts.values():
        if value != 0:
            return False
    return True

s1= "geeks"
s2 = "kseeg"
print(anagrams(s1,s2))