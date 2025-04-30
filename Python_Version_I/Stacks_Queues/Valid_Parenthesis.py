# Valid Parentheses

def isBalanced(exp):
    stack = []
    for i in range(len(exp)):
        if exp[i] =="(" or exp[i]=="{" or exp[i]=="[":
            stack.append(exp[i])
        else:
            if stack and ((stack[-1]=="(") and exp[i]==")") or ((stack[-1]=="{") and exp[i]=="}") or ((stack[-1]=="[") and exp[i]=="]"):
                stack.pop()
            else:
                return False
    return not stack

def isBalance(exp):
    stack=[]
    dicts={'{':'}','[':']','(':')'}
    for i in exp:
        if i in "{[(":
            stack.append(i)
        else:
            if not stack:
                return False
            top = stack.pop()
            if dicts[top] is not i:
                return False
        return True if not stack else False

s = "{([])}"
print(isBalance(s)) 