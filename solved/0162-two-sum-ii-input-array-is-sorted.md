# Two Sum II - Input Array is Sorted

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](http://rb.gy/oual6h)

<br>
<br>

## Solution

<br>

### Brute Force

<br>

### Efficient Solution

- This is a $O(n)$ solution, as in the worst case the left pointer can reach to the last but one place in the entire array.

  ```py
  class Solution:
      def twoSum(self, numbers: List[int], target: int) -> List[int]:
          l = 0
          r = len(numbers)-1

          while numbers[l] + numbers[r] != target:
              addition = numbers[l] + numbers[r]
              if addition < target:
                  l += 1
              else:
                  r -= 1
          return [l+1, r+1]
  ```

<br>
<br>

## Resources

<br>
<br>
