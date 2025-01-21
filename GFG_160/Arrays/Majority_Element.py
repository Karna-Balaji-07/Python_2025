# majority element - II

''' 
You are given an array of integer arr[] where each number represents a vote to a candidate
Return the candidates that have votes greater than one-third of the total votes,
If there's not a majority vote, return an empty array. 

'''

def majority_element(arr):
    dicts = {}
    n = len(arr)
    arr.sort()
    for i in arr:
        if i not in dicts:
            dicts[i]  = arr.count(i)
    temp = []
    for key,value in dicts.items():
        if value > n//3:
            temp.append(key)
    return temp

arr = [1,2,3,4]
print(majority_element(arr))