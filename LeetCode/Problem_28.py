# Find the index of the first occurrance in a string

def indexs(haystack, needle):
    result = haystack.index(needle)
    return result

def indexs1(haystack, needle):
    n = len(haystack)
    m = len(needle)
    for i in range(n-m+1):
        if haystack[i:i+m] == needle:
            return i
    return -1
haystack = "hello"
needle = "ll"
print(indexs(haystack,needle))