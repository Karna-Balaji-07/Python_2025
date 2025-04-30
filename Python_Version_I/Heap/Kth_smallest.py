

class Solution:

    def kthSmallest(self, arr,k):
        maxi = max(arr)
        dicts = {}
        for num in arr:
            dicts[num] = dicts.get(num,0)+1
        count = 0
        for i in range(maxi+1):
            if i in dicts:
                count += dicts[i]
                if k <= count:
                    return i
        return -1
                
        
        

