# set matrices to zero

def matrix(arr):
    n=len(arr)
    m=len(arr[0])
    first_row_zero=False
    first_col_zero=False
    
    for row in range(n):
        for col in range(m):
            if arr[row][col]==0:
                if row==0:
                    first_row_zero=True
                if col==0:
                    first_col_zero=True
                arr[row][0] = arr[0][col] = 0

    for row in range(1,n):
        for col in range(1,m):
            arr[row][col] = 0 if arr[0][col]==0 or arr[row][0]==0 else arr[row][col]
    if first_row_zero:
        for col in range(m):
            arr[0][col]=0
    if first_col_zero:
        for row in range(n):
            arr[row][0] = 0
    return arr

arr=[[1,1,1],[1,0,1],[1,1,1]]
print(matrix(arr))
