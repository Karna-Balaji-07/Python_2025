# last stone weight

def solution(arr):
    while len(arr) > 1:
        arr.sort()
        first = arr.pop()
        second = arr.pop()
        if first == second:
            continue
        elif first != second:
            result = first - second
            arr.append(result)
    return arr

arr = [2,2]
print(solution(arr))
        