# the next smaller element in the array

def smaller(arr):
    n = len(arr)
    stack=[]
    result = [-1]*n
    for i in range(n):
        next_value = arr[i]
        while stack and arr[stack[-1]] >= next_value:
            result[stack.pop()] = next_value

        stack.append(i)
    return result

arr = [4, 8, 2, 1, 6, 10, 5]
print(smaller(arr))