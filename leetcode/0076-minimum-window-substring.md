# 76. Minimum Window Substring

Hard [level question on leetcode](https://leetcode.com/problems/minimum-window-substring/description/).

<br>
<br>
<br>

## Clarifications

1. What is the minimum and maximum lenght of the input strings?
   - 1 <= m, n <= 105

1. What are the characters like in the input strings?
   - s and t consist of uppercase and lowercase English letters.

<br>
<br>
<br>

## Test cases

| Case                | Input                  | Output |
| ------------------- | ---------------------- | ------ |
| answer at end       | s="xaxbxcxabc" t="abc" | "abc"  |
| answer in middle    | s="xaxbxabcxc" t="abc" | "abc"  |
| no answer           | s="abc" t="aa"         | ""     |
| consider duplicates | s="xabxaa" t="aab"     | "bxaa" |
| exact match         | s="abc" t="abc"        | "abc"  |

<br>
<br>
<br>

## Solution

<br>
<br>

### Quadratic solution

```py
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetMap = defaultdict(int)
        for ch in t:
            targetMap[ch] += 1

        def isConditionSatisfied(map):
            for char in targetMap:
                if char not in map:
                    return False
                elif targetMap[char] > map[char]:
                    return False
            return True

        checkMap = defaultdict(int)
        for ch in s:
            checkMap[ch] += 1

        if not isConditionSatisfied(checkMap):
            return ""

        res = s
        left = 0
        windowMap = defaultdict(int)
        for right in range(len(s)):
            ch = s[right]
            windowMap[ch] += 1

            while(isConditionSatisfied(windowMap)):
                if (len(s[left: right+1]) < len(res)):
                    res = s[left:right+1]

                windowMap[s[left]] -= 1
                left += 1

        return res
```

```cpp

```

<br>

#### Explanation

Use two pointer sliding window technique.

- Create a map of character to frequency for the string 't'.
- Expand right pointer towards the right iteratively.
  - Populate the map of charcter to frequency for the current window.
  - If the condition is satisfied, update the result and shrink the window by moving the left pointer towards right.

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(m^2)$ solution in terms of time, where $m$ is llength of string 's'.
  - Creation of `targetMap` is $O(n)$.
  - Creation of `checkMap` is $O(m)$.
  - The for loop is $O(m) + O(m) = O(m)$.
    - The right pointer moves only forward "m" times. The left pointer also moves only forward "m" times (worst case) and not m times per right step!
    - The string slicing is an $O(m)$ operation in the worst case.
    - The function `isConditionSatisfied` can be considered a constant time operation because of the constraint (only lower and uppercase alphabets), Otherwise would have been a lienar operation.
  - Overall, $O(n) + O(m) + O(m)*O(m)  = O(m^2)$

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is size of the maps.

<br>

#### Analysis

- The `isConditionSatisfied` logic can be avoided.
- The string slicing can be avoided.
- `checkMap` and early return can be avoided.

<br>
<br>

### Linear solution

```py
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        targetMap = defaultdict(int)
        for ch in t:
            targetMap[ch] += 1

        have = 0
        needed = len(targetMap)

        windowMap = defaultdict(int)
        resLen = float('inf')
        resStart = 0
        left = 0

        for right, ch in enumerate(s):
            windowMap[ch] += 1
            if ch in targetMap and windowMap[ch] == targetMap[ch]:
                have += 1

            while have == needed:
                if right - left + 1 < resLen:
                    resLen = right - left + 1
                    resStart = left

                leftCh = s[left]
                windowMap[leftCh] -= 1
                if leftCh in targetMap and windowMap[leftCh] < targetMap[leftCh]:
                    have -= 1
                left += 1

        return "" if resLen == float('inf') else s[resStart: resStart + resLen]
```

```cpp

```

<br>

#### Explanation

Use two pointer sliding window technique.

- Create a map of character to frequency for the string 't'.
- Expand right pointer towards the right iteratively.
  - Populate the map of charcter to frequency for the current window.
  - If the condition is satisfied (the window contains all of t's characters)
    - Update the result via `resStart` for tracking starting index and `resLen` for determining ending index.
    - shrink the window by moving the left pointer towards right.
  - Update the `have` and `needed` variables in each step.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(m)$ solution in terms of time, where $m$ is llength of string 's'.
  - Creation of `targetMap` is $O(n)$.
  - The for loop is $O(m) + O(m) = O(m)$.
    - The right pointer moves only forward "m" times. The left pointer also moves only forward "m" times (worst case) and not m times per right step!

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is space used by maps.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- The time complexity of string slicing is O(k), where k is the length of the slice (the number of characters being extracted).
- To track the result, instead of using the string itself. It's better to use the starting and ending index variables and then form the result string at the end. Starting index and length of the result is pretty much the same.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
