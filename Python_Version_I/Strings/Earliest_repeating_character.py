# Find the earliest repeating character

def earliest(s):
    arrs = []
    for i in s:
        if i != " ":
            arrs.append(i) 
    arr = []
    for i in arrs:
        if i not in arr:
            arr.append(i)
        else:
            return i
        
s = "hello geeks"
print(earliest(s))