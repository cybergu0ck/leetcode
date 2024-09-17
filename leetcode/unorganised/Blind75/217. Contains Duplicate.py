from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
        
        for i in freq.values():
            if i>1:
                return True
        
        return False
        
    
            