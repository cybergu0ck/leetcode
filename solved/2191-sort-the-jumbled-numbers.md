# Sort the Jumbled Numbers

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/sort-the-jumbled-numbers/description/).

<br>
<br>

## Solution

<br>

### Brute Force

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>

### Efficient Force

- The following has $O(n*d + n*logn)$ time complexity $O()$ space complexity, where $n$ is the number of integers in nums and $d$ is the total number of digits.

  ```py
  class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []

        for index,num in enumerate(nums):
            text = str(num)
            encoded_num = 0
            for char in text:
                encoded_num *= 10
                encoded_num += mapping[int(char)]
            pairs.append((encoded_num, index))

        pairs.sort() #python's sort will sort based on first value of the tuple, it'll choose second value in case of tie
        return [ nums[item[1]] for item in pairs]
  ```

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>
<br>

## Notes

- Python list's sort method, specifically when the items are tuples, sorts the tuples based on the first value. It will automatically consider second value if there is a tie.

  ```py
  pairs = [(1,2), (2,4), (1,1)]
  pairs.sort()
  print(pairs)

  #[(1, 1), (1, 2), (2, 4)]
  ```

<br>
<br>

## Test Cases

- Test cases doesnt play a major role for finding solution.

<br>
<br>

## Resources

<br>
<br>
