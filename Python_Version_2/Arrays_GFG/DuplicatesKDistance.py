# Duplicates within K distance in an array

def duplicates1(arr,k):
    sets = set()
    for i in range(len(arr)):
        if arr[i] in sets:
            return True
        sets.add(arr[i])

        if i >= k:
            sets.remove(arr[i-k])
    return False


def sols(arr,k):
    arrs = []
    for i in range(len(arr)):
        if arr[i] in arrs:
            return True
        arrs.append(arr[i])

        if i >= k:
            arrs.remove(arr[i-k])
    return False
arr = [1,2,3,8,9,0,6,5,1,2]
print(sols(arr,3))