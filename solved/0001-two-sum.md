# Two Sum

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/two-sum/description/)

<br>
<br>

## Solution

<br>

### Brute Force

- This is a $O(n^2)$ solution.

  ```py
  from typing import List

  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          for i, v in enumerate(nums):
              for j, w in enumerate(nums):
                  if i != j:
                      if v + w == target:
                          return [i, j]


  answer = Solution()
  print(answer.twoSum([2, 7, 11, 15], 9))

  # [0,1]
  ```

<br>

### Efficient Solution

- This is a $O(n)$ solution, considering that the average-case time complexity to check if a key is present in a dictionary is $O(1)$.

  ```py
  from typing import List

  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          map = {}
          for index, value in enumerate(nums):
              needed = target - value
              if needed in map:
                  return [index, map[needed]]
              map[value] = index

  answer = Solution()
  print(answer.twoSum([2, 7, 11, 15], 9))
  # [0,1]
  ```

<br>
<br>

## Resources

<br>
<br>
