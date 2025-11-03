# Stable binary sort

def solution1(arr):
    even = []
    odd = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    
    result =[]
    result = even + odd
    return result


arr = [1,2,3,4,5,6]
print(solution1(arr))