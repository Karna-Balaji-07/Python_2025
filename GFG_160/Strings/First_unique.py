# First Non Repeating character

def unique(s):
    s = sorted(s)
    dicts = {}
    for i in s:
        if i not in dicts:
            dicts[i]= s.count(i)
    for key,value in dicts.items():
        if value == 1:
            return key
    return -1

def unique1(s):
    dicts = {}
    for i in s:
        dicts[i] = dicts.get(i,0)+1
    for i in s:
        if dicts[i] ==1:
            return i
    return -1

s = "geeksforgeeks"
print(unique(s))
print(unique1(s))