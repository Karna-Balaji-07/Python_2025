# Reverse the order of words without reversing the words

def reverses(s):
    s=s.strip()
    arr = s.split()
    arr.reverse()
    result=  " ".join(arr)
    print(result)



reverses(" pqr mno ")