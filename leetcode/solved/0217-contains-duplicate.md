# 217. Contains Duplicate

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/contains-duplicate/description/).

<br>
<br>

## Solution

<br>

### Brute Force

- The following has $O(n^2)$ time complexity $O(1)$ space complexity.

  ```py
  class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for index1 in range(len(nums)):
            for index2 in range(len(nums)):
                if index1 != index2 and nums[index1] == nums[index2]:
                    return True
        return False
  ```

<br>

### Efficient Solution

- The following has $O(n)$ time complexity $O(n)$ space complexity.

  ```py
  class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True
            else:
                unique_nums.add(num)
        return False
  ```

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>
<br>

## Notes

- We can sort the array and then check the difference between two consecutive items, if it's zero then it means it is a duplicate. This will have $O(n*log(n))$

<br>
<br>

## Test Cases

<br>
<br>

## Resources

<br>
<br>
