# Longest Common Prefix

def prefix(arr):
    arr.sort()
    n=len(arr)
    first=arr[0]
    last=arr[-1]
    minLengtht= min(len(first),len(last))
    i=0
    while i < minLengtht and first[i]==last[i]:
        i+=1
    return first[:i]

arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
print(prefix(arr))
