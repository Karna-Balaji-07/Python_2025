# Daily temperatures

def temperatur(arr):
    result = [0] * len(arr)
    stack = []
    for i in range(len(arr)-1,-1,-1):
        curr_temp = arr[i]
        while stack and curr_temp >=  arr[stack[-1]]:
            stack.pop()
        if stack:
            result[i] = stack[i]-1
        stack.append(i)
    return result


def temperature(arr):
    result = [0]*len(arr)
    n = len(arr)
    for i in range(n-2,-1,-1):
        j = i+1
        while j < n and arr[i] >= arr[j]:
            if result[j] > 0:
                j += result[j]
            else:
                j = n
        if j < n:
            result[i] = j-i
    return result
    