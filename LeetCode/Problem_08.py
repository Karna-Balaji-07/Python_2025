# Atoi String to integer

def solution(s):

    s = s.strip()
    if len(s) == 0:
        return 0
    
    result = ""
    num = "1234567890"
    sign = ""
    
    for i in s:
        if i in '+-' and len(result) == 0 and len(sign) == 0:
            sign = i
        elif i in num:
            result += i
        else:
            break
    
    if len(result) == 0:
        return 0
    
    result = sign + result
    
    if int(result) > 2**31-1:
        return 2**31-1
    elif int(result) < -2**31:
        return -2**31
    else:
        return int(result)
    
def solution2(s):
    s = s.strip()
    if not s:
        return 0
    if s[0] == '-':
        sign = -1
    else:
        sign = 1
    if s[0] in ['+', '-']:
        s = s[1:]
    num = 0
    for i in s:
        if not i.isdigit():
            break
        num = num*10+ int(i)
        num = num*sign  
    if num > 2**31-1:
        return 2**31-1 
    elif num < -2**31:
        return -2**31
    else:
        return num
    
s = "42"
print(solution2(s)) 