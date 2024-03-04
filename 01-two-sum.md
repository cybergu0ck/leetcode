## Description

Two Sum problem from [leetcode](https://leetcode.com/problems/two-sum/description/).

<br>
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
          for i, v in enumerate(nums):
              needed = target - v
              if v in map:
                  return [map[v], i]
              map[needed] = i


  answer = Solution()
  print(answer.twoSum([2, 7, 11, 15], 9))

  # [0,1]
  ```
