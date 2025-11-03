# 125. Valid palindrome

def solution1(s):
    arr = ""
    for i in s:
        if i.isalnum():
            arr += i.lower()
    return arr[::-1] == arr

s = "A man, a plan, a canal: Panama"
print(solution1(s))