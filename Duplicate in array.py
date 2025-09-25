class Solution:
    def findDuplicates(self, arr):
        
        
        arr2 = []
        
        seen = set()
        
        for i in arr:
            
            if i in seen:
                
                arr2.append(i)
                
            else:
                
                seen.add(i)
                
        return arr2