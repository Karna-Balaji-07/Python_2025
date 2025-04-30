# Binary String

def binary(s):
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == "1":
            for j in range(i+1,n):
                if s[i] == s[j]:
                    count += 1
                
    return count

def binary1(s):
    n = len(s)
    arr = []
    for i in s:
        arr.append(i)
    count = arr.count("1")
    formula = (count * (count-1)) // 2
    return formula

s = "1111"
print(binary(s))
print(binary1(s))