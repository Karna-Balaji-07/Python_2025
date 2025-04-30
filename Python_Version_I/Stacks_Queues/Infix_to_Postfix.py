# Conversion from Infix expression to Postfix expression

def precedence(c):
    if c=='^':
        return  3
    elif c=='/' or c=='*':
        return 2
    elif c =='+' or c=='-':
        return 1
    else:
        return 1
    

def infixPostfix(s):
    stack=[]
    result = ""
    for i in range(len(s)):
        c = s[i]
        if (c>='a'and c<= 'z') or (c>='A' and c<='Z') or (c>='0' and c<='9'):
            result+=c

        elif c=='(':
            stack.append('(')
        elif c==')':
            while stack[-1] != '(':
                result+=stack.pop()
            stack.pop()

        else:
            while stack and (precedence(c)<= precedence(stack[-1])) :
                result+=stack.pop()
            stack.append(c)
    while stack:
        result+=stack.pop()
    print(result)

exp = "a+b*(c^d-e)^(f+g*h)-i"
infixPostfix(exp)