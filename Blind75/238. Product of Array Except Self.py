class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        
        premul = nums[0]
        for i in range(1, len(nums)):
            res[i] = premul
            premul *= nums[i]
        
        postmul = nums[-1]
        for i in range(len(nums)-2, -1,-1):
            res[i] *= postmul
            postmul *= nums[i]
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        