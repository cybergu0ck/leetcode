class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s = (''.join(ch for ch in s if ch.isalnum())).lower()
        
        res = True if new_s[::-1] == new_s else False
        
        return res
        
        
        
        