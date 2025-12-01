# split an array into 3 equal segments

def solution1(arr):
    n = len(arr)
    sums = sum(arr)
    if sums % 3 != 0:
        return [-1,-1]

    third = sums // 3

    curr = 0
    result = []
    for i in range(len(arr)):
        curr += arr[i]
        if curr == third:
            result.append(i)
            curr = 0
            print("Result : ",result)

            if len(result) == 2 and i < len(arr)-1:
                return result

    return [-1,-1]

