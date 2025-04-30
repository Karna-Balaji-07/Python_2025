# Distinct Elements in an array

def distinct1(arr):
    temp = []
    for i in arr:
        if i not in temp:
            temp.append(i)
    return temp

arr = [1,2,2,3,2,4,4,5]
print(distinct1(arr))