# 5. Longest Palindromic Substring

Medium [level question on leetcode](https://leetcode.com/problems/longest-palindromic-substring/description/).

<br>
<br>
<br>

## Clarifications

- Clarify the definition of palindrome.

  - A string is a palindrome if it reads the same forward and backward.

- Clarify the definition of a substring.

  - A contigious sequence of characters of the string.

- If the input string consists of more than one palindromic substring with same longest length, what should be returned?

  - Return any of the longest palindromic substring.

- Can the string be empty? If yes, what must be the expected output?

  - No, input strings are not empty.

- What are the characters of the input string like?

  - Consists of lowercase English letters.

<br>
<br>
<br>

## Test cases

| Case                                   | Input    | Output    |
| -------------------------------------- | -------- | --------- |
| single character is a palindrome       | "a"      | "a"       |
| single character palindromic substring | "ab"     | "a" or "b |
| odd length palindromic substring       | "zabax"  | "aba"     |
| even length palindromic substring      | "zabbax" | "abba"    |

- These test cases should cover all the scenarios.

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1] #slicing to get the reverse is also O(n)
                backwards = substring[::-1]
                if(substring == backwards):
                    cur = substring
                    if(len(cur)> len(longest)):
                        longest = cur

        return longest
```

```cpp

```

<br>

#### Explanation

Check if every possible substring is a palindrome.

- Every possible substring is got using two nested loops.
- One a substring is got, check if it is a palindrome and update the longest palindromic substring.

<br>

#### Complexity analysis

- Time Complexity : This is a cubic, $O(n^3)$ solution in terms of time, where $n$ is size of the input string.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

### Quadratic solution

```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        res_len = 0

        for i in range(len(s)):
            #odd length substrings
            l, r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > res_len:
                    res = s[l:r+1]
                    res_len = len(res)
                l -= 1
                r += 1

            #even length substrings
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > res_len:
                    res = s[l:r+1]
                    res_len = len(res)

                l -= 1
                r += 1

        return res
```

```cpp

```

<!-- TODO - complete the cpp implementation -->

<br>

#### Explanation

For every character in the string, create left and right pointers and expand it outwards to check if it's a palindrome.

- Iterate over the characters of the input string.
- For every character, initialise the left and right pointers.
- Until the pointers are valid and the characters pointed to by the pointers are same. Update the longest palindromic substring and expand the pointers outwards.
- We need to do the same thing twice with different initialisations of left and right pointers for the odd and even palindromic substrings.

<br>

- The core logic used here is exactly same as that of [leetcode 647, Palindromic Subtrings](./0647-palindromic-substrings.md), The only change is that instead of keeping track of the count, we keep track of the longest palindromic substring.

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(n^2)$ solution in terms of time, where $n$ is the size of the input string.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

- [leetcode 647, palindromic substrings](./0647-palindromic-substrings.md) is a good follow up question for this.

<br>
<br>
<br>

## Notes

- Know how to check if a string is a palindrome. See [leetcode 242, Valid Palindrome](./0242-valid-anagram.md)

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
