# Valid parantheses

''' 
The idea is to store all the opening brackets in a stack and then check if the opening and closing brackets match
we creat a dictionary where closing brackets are keys and opening are values.
if stack is empty or last element of stack which is the opening bracket does not match the opening bracket of the dict then returns false
then pops the stack if true
returns whether the stack is empty or not


'''

def parantheses(s):
    stack = []
    dicts = {'}':'{', ']':'[',')':'('}
    for i in s:
        if i in "[{(":
            stack.append(i)
        else:
            if not stack or stack[-1] != dicts[i]:
                return False
            stack.pop()
    return not stack

    



s = "(])"
print(parantheses(s))