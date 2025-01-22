# Missing and repeating elements in a array

def Missing_repeating1(arr):
    n=len(arr)
    dicts={}
    result=[]
    for i in arr:
        dicts[i]=arr.count(i)
    for key,value in dicts.items():
        if value > 1:
            result.append(key)
    for i in range(1,n+1):
        if i not in arr:
            result.append(i)
    return result


def Missing_repeating2(arr):
    n=len(arr)
    result=[]
    arr.sort()
    for i in range(1,n):
        if arr[i-1] == arr[i]:
            result.append(arr[i])
    for i in range(1,n+1):
        if i not in arr:
            result.append(i)
    return result

def Missing_repeating3(arr):
    n=len(arr)
    sums =  n*(n+1)//2
    for i in range(n):
        if arr[abs(arr[i])-1]>0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
            sums -= abs(arr[i])
        else:
            repeating=abs(arr[i])
    return [repeating,sums]


arr =  [1, 3, 3] 
print(Missing_repeating1(arr))
print(Missing_repeating2(arr))
print(Missing_repeating3(arr))

