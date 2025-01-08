# Print all the duplicate characters in the string

def duplicate(s):
    dict = {}
    for i in s:
        dict[i] = s.count(i)
    for key,value in dict.items():
        if value > 1:
            print(f'{key}, Count = {value}')

s = "geeksforgeeks"
duplicate(s)