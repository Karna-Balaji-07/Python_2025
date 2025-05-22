# 2000. Reverse prfix of the word

def solution1(s,p):
    arr = []
    for i in s:
        arr.append(i)
    index = 0
    for i in range(len(arr)):
        if arr[i] == p:
            index = i
    
    arr = arr[:index+1][::-1] + arr[index+1:]

    return "".join(arr)

def solution2(s,p):
    index = 0
    for i in range(len(s)):
        if s[i] == p:
            index = i
            break
    
    result = s[:index+1][::-1] + s[index+1:]
    return result

s = "abcdefg"
p = "d"
print(solution2(s,p))