# Baseball game

def is_integer(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

def baseball(arr):
    result = []
    for i in arr:
        if is_integer(i):
            result.append(int(i))
        if i == 'C':
            result.pop()
        elif i == 'D':
            mul = 2*result[-1]
            result.append(mul)
        elif i == '+':
            adds = result[-1]+result[-2]
            result.append(adds)
        
    return sum(result)  

def baseball1(operations):
    a=[]
    for i in operations:
        if(i=="C"):
            a.pop()
        elif(i=="D"):
            a.append(2*a[-1])
        elif(i=="+"):
            a.append(a[-1]+a[-2])
        else:
            a.append(int(i))
    return sum(a)


arr = ["5","-2","4","C","D","9","+","+"]
print(baseball(arr))      