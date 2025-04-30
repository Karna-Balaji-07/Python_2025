# Second most repeated element

def second(arr):
    n = len(arr)
    dict = {}
    for i in arr:
        if i not in dict:
            dict[i] = arr.count(i)
    index = list(dict.values())
    index.sort(reverse=True)
    res = index[1]
    for key,value in dict.items():
        if value == res:
            return key
    return 0

arr = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
print(second(arr))