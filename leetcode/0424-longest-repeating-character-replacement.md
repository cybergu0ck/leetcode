# 424. Longest Repeating Character Replacement

Medium [level question on leetcode](https://leetcode.com/problems/longest-repeating-character-replacement/description/).

<br>
<br>
<br>

## Clarifications

- Clarify the definition of a substring.

  - A substring is a contigious non-empty sequence of characters within the string.

- Can the input string be empty? If yes what is the expected result?

  - No

- What kind of characters are present in the input string?

  - The string consists of only uppercase english characters.

<br>
<br>
<br>

## Test cases

| Case | Input            | Output |
| ---- | ---------------- | ------ |
|      | "AABB" and k=2   | 4      |
|      | "AABB" and k=1   | 3      |
|      | "AABB" and k=0   | 2      |
|      | "AABABB" and k=1 | 4      |

- Not fully sure if these cover all the cases.

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

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

```cpp

```

<br>

#### Explanation

<!-- one line desctiption of the logic of the algorithm -->
<!-- detailed explanation with steps if appropriate -->

<br>

#### Complexity analysis

- Time Complexity : This is a cubic, $O(n^3)$ solution in terms of time, where $n$ is size of the input string.
- Space Complexity : This is a linear, $O(m)$ solution in terms of space, where $m$ is number of unique characters in the input string.

<br>
<br>

### Linear solution

```py
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        char_to_freq = defaultdict(int)
        l = 0
        r = 0

        while(r != len(s)): # or use : for right in range(len(s)):
            char_to_freq[s[r]] += 1
            cur_len = r - l + 1
            replacable_len = cur_len - max(char_to_freq.values())
            if(replacable_len <= k):
                longest = max(longest, cur_len)
            else:
                l += 1
                char_to_freq[s[l]] -= 1
            r += 1
        return longest
```

```cpp

```

<!-- TODO - write the C++ version of this -->

<br>

#### Explanation

Use sliding window technique and a map with keys as character and the values as it's frequency.

1. Initialise the left and right pointers to point to the first character.
1. Iterate the right pointer until it reaches the right end.
1. Add the character pointed by right pointer to the map. key as the character and value is its frequency.
1. Calculate the replacable length, i.e. equal to current length - character that has highest frequency.
1. If the replacable length is less than or equal to "k", update result if needed.
1. If the replacable length is greater than "k", increment the left pointer and update the map accordingly.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is size of the input string.
- Space Complexity : This is a linear, $O(m)$ solution in terms of space, where $m$ is number of unique characters in the input string.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Solve [leetcode 3, longest substring without repeating characters](./0003-longest-substring-without-repeating-characters.md) first.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
