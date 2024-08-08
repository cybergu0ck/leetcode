# 213. House Robber II

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/house-robber-ii/description/).

- Some good clarification questions are:

<br>
<br>

## Solution

<br>

### Brute Force

```py

```

- The following has $O()$ time complexity $O()$ space complexity.

<br>

### Efficient Solution

```py
class Solution:
    def rob1(self,nums):
        rob1, rob2 = 0,0
        for num in nums:
            cur = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = cur
        return rob2

    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.rob1(nums[:-1]),self.rob1(nums[1:]))
```

- _"If we cut a circle and straighten it, we get a line"_. Applying the algorithm used for OG house robber cleverly.
- The following has $O(n)$ time complexity $O(1)$ space complexity.

<br>

### Ideal Solution

```py

```

- The following has $O()$ time complexity $O()$ space complexity.

<br>
<br>

## Notes

<br>
<br>

## Test Cases

<br>
<br>

## Resources

- credit to neetcode.

<br>
<br>
