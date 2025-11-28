# Find the maximum consecutive ones or zeros in an array

def solution(arr):
    ones = 0
    zeros = 0
    result1 = 0
    result0 = 0

    for i in arr:
        if i == 1:
            ones += 1
        else:
            result1 = max(ones, result1)
            ones = 0
        result1 = max(ones, result1)

    for i in arr:
        if i == 0:
            zeros += 1
        else:
            result0 = max(zeros, result0)
            zeros = 0

    return max(result0, result1)

arr =[0,0,1,0,1,0,1,1,1,1,1]
print(solution(arr))
