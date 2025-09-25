class Solution:
    def countDistinct(self, arr, k):
        l=[]
        max_len=[]
        for i in range(k):
            l.append(arr[i])
        max_len.append(len(set(l)))
        for j in range(k,len(arr)):
            l.pop(0)
            l.append(arr[j])
            max_len.append(len(set(l)))
        return max_len