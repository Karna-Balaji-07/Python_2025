# Reverse words in a string

def reverses(s):
    s = s.strip()
    stack = []
    arr = s.split(" ")
    for i in arr:
        if i != "":
            stack.append(i)
    s = " ".join(stack[::-1])
    print(s)

reverses("a good   example")