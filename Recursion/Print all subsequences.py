# print all subsequences

def subs(arr,index,res,ans):
    if index >= len(arr):
        ans.append(res.copy())
        return

    subs(arr,index+1, res + [arr[index]], ans)
    subs(arr,index+1, res, ans)

arr = [1,2,3]
ans = []
subs(arr,0, [], ans)
print(ans)
