# Container with most water

Leetcode medium level question.

<br>
<br>

## Description

Find it [here](http://rb.gy/oual6h)

<br>
<br>

## Solution

<br>

### Brute Force

- $O(n^2)$ solution.

<br>

### Efficient

- $O(n)$ solution using a two pointer technique.

  ```py
  class Solution:
      def maxArea(self, height: List[int]) -> int:
          l = 0
          r = len(height)-1
          maxArea = 0

          while(l<r):
              maxArea = max(maxArea, min(height[l], height[r])*(r-l))
              if height[l] < height[r]:
                  l+=1
              else:
                  r-=1
          return maxArea
  ```
