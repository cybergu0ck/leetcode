# 424. Longest Repeating Character Replacement

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/longest-repeating-character-replacement/description/).

- Some good follow ups are:

<br>
<br>

## Solution

<br>

### Brute Force

```py
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                freq = defaultdict(int)
                for c in s[i:j+1]:
                    freq[c] += 1
                length = len(s[i:j+1])
                max_repeated = max(freq.values())
                if length - max_repeated <= k:
                    res = max(res, length)
        return res
```

- The following has $O(n^3)$ time complexity $O(n)$ space complexity.

<br>

### Efficient Solution

```py
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = defaultdict(int)
        left = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            cur_len = right - left + 1
            max_repeat = max(freq.values())
            if cur_len - max_repeat <= k:
                res = max(res, cur_len)
            else:
                freq[s[left]] -= 1
                left += 1
        return res
```

- Solving the question using "Sliding Window Technique"

  1. Initialise left and right pointers, Here the right pointer is managed by the for loop and we manage only the left pointer.
  2. We add the character to the map in every iteration.
  3. The core logic is in the check, we get the character with maximum frequency in the current window. If (cur_len - max_repeat) <= 2, Then we can consider this as a favourable solution. Otherwise we have reached the bounds with the current window and need to slide the window forward by incrementing the left pointer and decrementing the correct key in the map.

- The following has $O(n)$ time complexity $O(n)$ space complexity.

<br>

### Ideal Solution

```py

```

- The following has $O()$ time complexity $O()$ space complexity.

<br>
<br>

## Notes

<br>
<br>

## Test Cases

<br>
<br>

## Resources

<br>
<br>
