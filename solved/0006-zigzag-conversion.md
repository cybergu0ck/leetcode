# 6. Zigzag Conversion

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/zigzag-conversion/description/).

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

- The following has $O(n)$ time complexity $O(n + r)$ space complexity, where 'n' is the number of characters in the string and 'r' is the numRows.

  ```py
  class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigZags = [[] for _ in range(numRows)]
        isDown = True
        row = 0
        for char in s:
            zigZags[row].append(char)
            if isDown:
                row += 1
            else:
                row -= 1
            if row == 0:
                isDown = True
            elif row == numRows -1:
                isDown = False

        res = ""
        for row in zigZags:
            res += ''.join(row)
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

- The solution is non-intuitive for the first time.

- The order of which among `row` and `direction` to update is not important, works both ways.

- Learnt that the following code creates the shallow copy! All the items in the twodarray refer to the same list.

  ```py
  twodarray = [[]] *3
  twodarray[0].append('a')
  print(twodarray)

  [['a'], ['a'], ['a']]
  ```

- Better way to achieve what is needed above is

  ```py
  twodarray = [[] for i in range(3)]
  twodarray[0].append('a')
  print(twodarray)
  [['a'], [], []]
  ```


<br>
<br>

## Test Cases

- When the numRows = 1, it is an edge case.

<br>
<br>

## Resources

- Checkout [greg hogg's video](https://www.youtube.com/watch?v=2NMMVnxV6lo)

<br>
<br>
