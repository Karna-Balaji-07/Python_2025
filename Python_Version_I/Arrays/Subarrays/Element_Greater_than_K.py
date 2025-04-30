# Count subarrays with all elements greater than K

def greater1(arr, element):
    count = 0
    number = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > element:
            count += 1
        else:
            number += count * (count+1) // 2
            count = 0
    
    if count:
        number += count * (count+1) //2
    return int(number)

arr = [3, 4, 5, 6, 7, 2, 10, 11]
element = 5
print(greater1(arr,element))

