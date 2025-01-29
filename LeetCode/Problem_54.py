# spiral matrix

def spiral(arr):
    n=len(arr)
    m=len(arr[0])

    result=[]
    top=0
    bottom=n-1
    left=0
    right=m-1

    while top <= bottom and left <= right:
        # printing from left to right
        for i in range(left,right+1):
            result.append(arr[top][i])
        top+=1

        # printing from top to bottom
        for i in range(top,bottom+1):
            result.append(arr[i][right])
        right-=1

        # Printing bottom row from right to left
        if top <= bottom:
            for i in range(right,left-1,-1):
                result.append(arr[bottom][i])
            bottom-=1

        # Printing bottom to top
        if left<=right:
            for i in range(bottom,top-1,-1):
                result.append(arr[i][left])
            left += 1

    return result

arr = [[1,2,3],[4,5,6],[7,8,9]]

print(spiral(arr))