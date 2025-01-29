#Merge intervals

def merge(arr):
    n=len(arr)
    m=len(arr[0])
    arr.sort(key=lambda x:x[0])
    result=[]
    current=arr[0]
    for i in range(n):
        if current[1] >= arr[i][0]:
            current[1] = max(current[1],arr[i][1])
        else:
            result.append(current)
            current=arr[i]
    result.append(current)
    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
        