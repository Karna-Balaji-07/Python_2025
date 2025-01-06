# Maximum length of the sub-array whose first and last elements are same

def maxs1(arr):
    n = len(arr)
    maxi = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                maxi = max(maxi, j-i+1)
    return  maxi

def maxs2(arr):
    n = len(arr)
    maxi = 0
    for start in range(n):
        for end in range(n-1,start-1,-1):
            if arr[start] == arr[end]:
                maxi = max(maxi, end-start+1)
                break
    return maxi

def maxs3(arr):
    dict = {}
    n = len(arr)
    maxi = 0
    for i,j in enumerate(arr):
        if j not in dict:
            dict[j] = i
        else:
            maxi = max(maxi, i-dict[j]+1)
    return maxi

arr= ["g","e","e","k","s"]
print(maxs1(arr))
print(maxs2(arr))
print(maxs3(arr))