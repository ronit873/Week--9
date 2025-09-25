class Solution:

    def countPairs(self,arr, target):
        
        d=dict()
        count=0
        
        for i in arr:
            if (target-i) in d:
                count+=d[target-i]
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        return count