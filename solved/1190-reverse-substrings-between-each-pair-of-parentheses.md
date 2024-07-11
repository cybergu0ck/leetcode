# Reverse Substrings Between Each Pair of Parentheses

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](http://rb.gy/0h2e8g).

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

- The following has $O(n^2)$ time complexity $O(n)$ space complexity.

  ```py
  class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ")":
                stack.append(c)
            else:
                rev = []
                cur = stack.pop()
                while cur != "(":
                    rev.append(cur)
                    cur = stack.pop()
                stack.extend(rev)

        return ''.join(stack)
  ```

  - The time of complexity is technically $O(n*m)$, where n is the length of the string and m is the length of the string inside the parentheses.

<br>

### Ideal Solution

//TODO - Code up the ideal O(n) solution explained in neetcode's yt video

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>
<br>

## Notes

<br>
<br>

## Resources

- Checkout [neetcode.io's video](https://www.youtube.com/watch?v=n_pCJmg-RyU)

<br>
<br>
