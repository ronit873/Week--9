class Solution:
    def longestConsecutive(self,arr):
        arr=sorted(set(arr))
        count=1
        ms=1
        arr.sort()
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]+1:
                count+=1
                ms=max(ms,count)
            else:
                count=1
        return ms