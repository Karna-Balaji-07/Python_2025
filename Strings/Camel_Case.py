# Convert Sentence to Camel Case

def convert(s):
    arr = s.split(" ")
    string = ""
    for i in range(len(arr)):
        if i != 0:
            string += arr[i].capitalize()
        else:
            string += arr[i]
    return string

s = "i love gfg"
print(convert(s))