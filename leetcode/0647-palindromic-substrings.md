# 647. Palindromic Substrings

Medium [level question on leetcode](https://leetcode.com/problems/palindromic-substrings/description/).

<br>
<br>
<br>

## Clarifications

- Clarify the definition of a palindrome.

  - A string is a palindrome when it reads the same backward as forward.

- Clarify the definition of a substring.

  - A substring is a contiguous sequence of characters within the string.

- Can the string be empty? If yes, what must be the expected output?

  - No, input strings are not empty.

- What are the characters of the input string like?

  - Consists of lowercase English letters.

<br>
<br>
<br>

## Test cases

| Case | Input   | Output |
| ---- | ------- | ------ |
|      | "a"     | 1      |
|      | "ab"    | 2      |
|      | "aa"    | 3      |
|      | "aa"    | 3      |
|      | "aaa"   | 6      |
|      | "abazx" | 6      |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py

```

```cpp

```

<br>

#### Explanation

Check if every possible substring is a palindrome.

- Every possible substring is got using two nested loops.
- One a substring is got, check if it is a palindrome and update the count.

<br>

#### Complexity analysis

- Time Complexity : This is a cubic, $O(n^3)$ solution in terms of time, where $n$ is size of the input string.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

### Quadratic solution

```py
class Solution:
    def countSubstrings(self, s: str) -> int:
            count = 0

            for i in range(len(s)):
                #odd length substrings
                l, r = i,i
                while l>=0 and r<len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1

                #even length substrings
                l, r = i, i+1
                while l>=0 and r<len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1

            return count
```

```cpp

```

<!-- TODO - complete the C++ implementations -->

<br>

#### Explanation

For every character in the string, create left and right pointers and expand it outwards to check if it's a palindrome.

- Iterate over the characters of the input string.
- For every character, initialise the left and right pointers.
- Until the pointers are valid and the characters pointed to by the pointers are same. Update the count and expand the pointers outwards.
- We need to do the same thing twice with different initialisations of left and right pointers for the odd and even palindromic substrings.

<br>

- The core logic used here is exactly same as that of [leetcode 5, Longest Palindromic Subtring](./0005-longest-palindromic-substring.md), The only change is that instead of keeping track of the longest palindromic substring, we keep track of the count.

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(n^2)$ solution in terms of time, where $n$ is size of the input string.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

- [leetcode 5, Longest Palindromic Subtring](./0005-longest-palindromic-substring.md) can be a good follow up.

<br>
<br>
<br>

## Notes

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
