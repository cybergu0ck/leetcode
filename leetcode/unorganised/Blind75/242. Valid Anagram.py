import collections 

class Solution:
        
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = collections.defaultdict(int)
        map2 = collections.defaultdict(int)
        
        for i in s:
            map1[i] += 1
        
        for j in t:
            map2[j] += 1
        
        
        if map1 == map2:
            return True
        else:
            return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        