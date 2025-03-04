#!/usr/bin/python3
# Using XOR instead of hashset


class Solution:
    def singleNumber(self, nums):
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        
        return res

result = Solution()
print(result.singleNumber([1,1,4,3,3]))   #Must return 4