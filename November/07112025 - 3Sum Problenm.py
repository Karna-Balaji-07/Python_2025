# 3 sum problem.. Find unique triplets that add upto zero

def solution1(arr):
    dicts = {}
    result = []
    for i in range(len(arr)):
        for j in range(1+i, len(arr)):
            value = -1 * (arr[i]+arr[j])
            if value in dicts:
                for k in dicts[value]:
                    result.append([k,i,j])

        if arr[j] not in dicts:
            dicts[arr[j]] = []

        dicts[arr[j]].append(j)

    return result