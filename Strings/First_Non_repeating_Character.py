# First Non repeating character

def nonRepeating(s):
    dict = {}
    for i in s:
        dict[i] = s.count(i)
    for key,value in dict:
        if value == 1:
            return key
    return -1