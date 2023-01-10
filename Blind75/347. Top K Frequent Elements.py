import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)
        
        for i in nums:
            freq[i] += 1
            
        freq = dict(sorted(freq.items(), key = lambda item:item[1], reverse = True))
        
        res = []
        
        count = 0
        
        for i, v in enumerate(freq):
            if count < k:
                res.append(v)
            count +=1
        
        return res
        
        