# 128. Longest Consecutive Sequence

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/longest-consecutive-sequence/description/).

<br>
<br>

## Solution

<br>

### Brute Force

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>

### Efficient Solution

- The approach is :
  - Iterate over the numbers
  - Check if (number-1) exists in the sequence, If it doesn't exist then the number can be a starting point for a continous sequence. 
  - Keep adding 1 to it and check if it exists in the given sequence.
  
- The following has $O(n)$ time complexity $O(1)$ space complexity. The time complexity may look like $O(n^2)$, but for the numbers for which the inner loop is ran, it won't be run again the next time. The space complexity is $O(1)$ without considering the given array, which we use as a set.

  ```py
  class Solution:
      def longestConsecutive(self, nums: List[int]) -> int:
          numset = set(nums)  #O(n)
          res = 0
          for num in nums:
              if num-1 not in numset:
                  length = 1
                  while num + length in numset:
                      length += 1
                  res = max(res, length)
          return res
  ```

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>
<br>

## Notes

- Converting a list to a set in python. This is a $O(n)$ time operation.

  ```py
  nums = [1,2,3,1,2,3]
  numset = set(nums)
  print(numset)

  #{1, 2, 3}
  ```

<br>
<br>

## Test Cases

- The solution is not driven by test case.

<br>
<br>

## Resources

- Checkout [neetcode's video](https://www.youtube.com/watch?v=P6RZZMu_maU)

<br>
<br>
