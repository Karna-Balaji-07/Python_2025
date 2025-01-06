# Multiplication of two square or rectangle matrices

def multiply(a,b):
    r1 = len(a)
    c1 = len(a[0])
    r2 = len(b)
    c2 = len(b[0])

    if c1 != r2:
        print("Result Invalid")
    result = [[0]*c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += a[i][k] * b[k][j]
    return result

a = [[1,1,1],[2,2,2],[3,3,3]]
b = [[3,3,3],[1,1,1],[2,2,2]]
print(multiply(a,b))