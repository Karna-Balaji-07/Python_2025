# Add 2 binary strings

def trim_leading_zeros(s):
    firstOne = s.find('1')
    return s[firstOne:] if firstOne != -1 else '0'

def binary_Strings(s1,s2):
    s1 = trim_leading_zeros(s1)
    s2= trim_leading_zeros(s2)
    n= len(s1)
    m=len(s2)
    if n < m:
        s1,s2=s2,s1
        n,m=m,n
    j=m-1
    carry=0
    result=[]

    for i in range(n-1,-1,-1):
        bit1=int(s1[i])
        bitsum = bit1+carry

        if j >=0:
            bit2= int(s2[j])
            bitsum += bit2
            j-=1
        bit = bitsum%2
        carry=bitsum//2
        result.append(str(bit))
    if carry > 0:
        result.append('1')
    
    return "".join(result[::-1])

s1 = "1101"
s2 = "111"
print(binary_Strings(s1,s2))
