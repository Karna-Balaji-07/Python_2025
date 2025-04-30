# Magnetic force between two balls

def solution(arr,m):
    first = min(arr)
    n = len(arr)
    findex = 0
    last = max(arr)
    lindex = n-1
    if m == 2:
        return last - first
    mid = (findex+lindex) // 2
    result = []
    
    return -1

arr = [1,2,3,4,7]
print(solution(arr,3))
