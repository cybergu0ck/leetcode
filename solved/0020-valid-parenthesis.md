# Valid Parentheses

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://rebrand.ly/qxlndaw).

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

- The following has $O(n)$ time complexity $O(n)$ space complexity using a map and stack.

  ```py
  class Solution:
    def isValid(self, s: str) -> bool:
        map = {"(": ")", "{":"}", "[":"]"}
        my_stack = []
        for char in s:
            if char in map:
                my_stack.append(char)
            else:
                if not my_stack:
                    return False
                popped = my_stack.pop()
                ans = map[popped]
                if char != ans:
                    return False
        if my_stack:
            return False
        else:
            return True
  ```

- A better version, The following has $O(n)$ time complexity $O(n)$ space complexity using a set and stack.

  ```py
  class Solution:
    def isValid(self, s: str) -> bool:
        opens = ('(', '{','[')
        stack = []
        for c in s:
            if c in opens:
                stack.append(c)
            elif c == ')' and stack and stack.pop() == '(':
                continue
            elif c == '}' and stack and stack.pop() == '{':
                continue
            elif c == ']' and stack and stack.pop() == '[':
                continue
            else:
                return False
        return not stack
  ```

<br>

### Ideal Solution


<br>
<br>

## Notes

- Potential perms and combs are as follows : "{()}" , "{", "}", "}{", "{]"

<br>
<br>

## Resources

<br>
<br>
