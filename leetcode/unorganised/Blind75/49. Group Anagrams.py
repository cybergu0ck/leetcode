import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         
        hashMap = collections.defaultdict(list) # This is to group the anagrams
        
        for word in strs:
            freq = [0] *26
            for letter in word:
                freq[ord(letter) - ord('a')] += 1
            
            hashMap[tuple(freq)].append(word)
        
        return hashMap.values()
            
        
        