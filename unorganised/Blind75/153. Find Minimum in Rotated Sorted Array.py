'''https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/'''

class Solution:
    def findMin(self, nums: list[int]) -> int:
        """return the smallest number in O(logn)."""
        left, right, cur_min = 0, len(nums)-1, nums[0]

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
                cur_min = min(cur_min, nums[left], nums[right], nums[mid])
                
            else:
                right = mid -1
                cur_min = min(cur_min, nums[left], nums[right], nums[mid])
        return cur_min

