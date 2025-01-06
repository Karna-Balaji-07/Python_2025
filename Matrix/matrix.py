# Matrix

rows = 3
cols = 3
arr = [[1]*cols]*rows
print(arr)

arr2 = [[1,2,3],[4,5,6],[7,8,9]]

# Accessing elements in a matrix
first_row = arr2[0]
first_row_first_column = arr2[0][0]
x = arr2[1][2]
y = arr2[2][2]
print(first_row,first_row_first_column,x,y,sep=", ")

# Traversal of a matrix
for i in range(len(arr2)):
    for j in range(len(arr2)):
        print(arr2[i][j],end=" ")
    print()

for row in arr2:
    for i in row:
        print(i,end=" ")
    print()


# Searching in an array : 
arr = [
    [0, 6, 8, 9, 11],
    [20, 22, 28, 29, 31],
    [36, 38, 50, 61, 63],
    [64, 66, 100, 122, 128]
]
element = 50
row = len(arr)
col = len(arr[0])
for i in range(row):
    for j in range(col):
        if arr[i][j] == element:
            print(i,j,sep="<=>")

