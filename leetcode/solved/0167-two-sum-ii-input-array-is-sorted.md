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

### Efficient Force

- The following has $O(n)$ time complexity $O(n)$ space complexity.

    ```py
    class Solution:
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
            track = dict()
            for index, value in enumerate(numbers):
                needed = target - value
                if(needed in track):
                    return [track[needed],index+1]
                else:
                    track[value] = index+1
    ```

<br>


### Ideal Solution

- The following has $O(n)$ time complexity $O(1)$ space complexity.

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
  - In the worst case the left pointer can reach to the last but one place in the entire array.

<br>
<br>

## Resources

<br>
<br>
