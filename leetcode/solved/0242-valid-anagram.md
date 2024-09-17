# Valid Anagram

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/valid-anagram/description/).

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

- The following has $O(n)$ time complexity $O(n)$ space complexity.

  ```py
  from collections import defaultdict

  class Solution:
      def isAnagram(self, s: str, t: str) -> bool:
          if len(s) != len(t):
              return False
          else:
              frequency_s = defaultdict(int)
              frequency_t = defaultdict(int)
              for char in s:
                  frequency_s[char] += 1
              for char in t:
                  frequency_t[char] += 1
              if frequency_s != frequency_t:
                  return False
          return True
  ```

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>
<br>

## Notes

- Know how to use a python's `defaultdict`

  ```py
  from collections import defaultdict

  map = defaultdict(int)
  ```

<br>
<br>

## Test Cases

<br>
<br>

## Resources

<br>
<br>
