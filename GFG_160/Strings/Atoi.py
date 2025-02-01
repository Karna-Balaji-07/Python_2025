# Atoi function to convert string to integer

def atoi(s):
    sign=1
    result=0
    index=0

    while index < len(s) and s[index]=="-":
        index+=1
    if index < len(s) and (s[index]=='-'or s[index]=='+'):
        if(s[index]=='-'):
            sign = -1
    index +=1

    while index < len (s) and '0' <= s[index] <= '9':
        res = 10*result+ (ord(s[index])-ord('0'))
        if res > (2**31-1):
            return sign * (2**31-1) if sign==1 else -2**31
        index +=1
    return result * sign

s="-1231"
s="42"
print(atoi(s))