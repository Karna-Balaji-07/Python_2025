# Sum of all subarrays

def sums(arr):
    n = len(arr)
    temp = []
    for i in range(n):
        for j in range(i,n):
            temp.append(arr[i:j+1])
    count = 0
    for i in range(len(temp)):
        count += sum(temp[i])
    return count

def sums2(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i,n):
            count += sum(arr[i:j+1])
    counts = count % (10**9 + 7)
    return counts

def sums3(arr):
    n = len(arr)
    index = 0
    count = 0
    for i in range(n):
        index = i
        while index < n:
            count += sum(arr[i:index+1])
            index += 1
        
    return count

def sums4(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        result += arr[i] * (i+1) * (n-i)
    return result

arr = [1,2,3]
print(sums2(arr))
print(sums(arr))
print(sums3(arr))
print(sums4(arr))