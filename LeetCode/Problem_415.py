# add two strings

def addition(s1,s2):
    n=len(s1)-1
    m=len(s2)-1
    result=[]
    carry=0
    while n  >=0 or m>=0 or carry:
        num1= ord(s1[n])-ord('0') if n >=0 else 0
        num2 = ord(s2[m])-ord('0') if m >= 0 else 0

        sums=num1+num2+carry
        digit=sums%10
        carry=sums//10
        result.append(str(digit))

        n-=1
        m-=1
    res=''.join(result[::-1])
    return res


s1="11"
s2="123"
print(addition(s1,s2))