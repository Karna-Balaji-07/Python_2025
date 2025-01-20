# Post fix to infix conversion

def isOperator(c):
    if (c>='a' and c<='z') and (c>='A' and c<='Z'):
        return True
    return False


def infix(exp):
    stack = []
    for i in exp:
        if isOperator(i):
            stack.insert(0,i)
        else:
            op1 = stack[0] 
            stack.pop(0) 
            op2 = stack[0] 
            stack.pop(0) 
            str =  op2+i+op1
            stack.insert(0,str)
    return stack[0]

exp = "ab*c+"
print(infix(exp))