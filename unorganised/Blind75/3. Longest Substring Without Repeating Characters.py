class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = []
        res = 0
        
        for literal in s:
            if literal not in track:
                track.append(literal)
                res = max(res, len(track))
            else:
                res = max(res, len(track))
                while(literal in track):
                    track.pop(0)
                track.append(literal)
        return res
    
        
            
                
        