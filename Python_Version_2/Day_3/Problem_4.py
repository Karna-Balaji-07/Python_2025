# 557. Reverse words in a string III

def solution1(s):
    arr = s.split()
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
    return " ".join(arr)

s = "Hello to the world"
print(solution1(s))