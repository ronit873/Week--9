class Solution:
    def twoSum(self, arr, target):
        seen={}
        for i,num in enumerate(arr):
            com = target-num
            if com in seen:
                return[seen[com],i]
            seen[num]=i
        return False