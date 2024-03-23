# Longest Substring Without Repeating Characters

medium level problem on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

<br>
<br>

## Solution

<br>

### Brute Force

- $O(n^2)$ solution.

  ```py
  class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
          longest = 0
          for i, v in enumerate(s):
              longest = max(longest, 1)
              new = v
              for w in s[i + 1 :]:
                  if w not in new:
                      new += w
                  else:
                      longest = max(longest, len(new))
                      break
              longest = max(longest, len(new))
          return longest


  answer = Solution()
  print(answer.lengthOfLongestSubstring("abcabcbb"))
  ```

<br>

### Efficient

- $O(n)$ solution using a dictionary and sliding window technique.

  ```py
  class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:

          start = result = 0
          seen = dict()

          for i, c in enumerate(s):

              if seen.get(c, -1) >= start:
                  start = seen[c] + 1

              result = max(result, i - start + 1)
              seen[c] = i

          return result


  answer = Solution()
  print(answer.lengthOfLongestSubstring("abcabcbb"))
  ```

- This is neetcode's solution I beleive.

  ```py
  class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
          track = []
          res = 0

          for literal in s:
              if literal not in track:
                  track.append(literal)
                  res = max(res, len(track))
              else:
                  res = max(res, len(track))
                  while(literal in track):
                      track.pop(0)
                  track.append(literal)
          return res
  ```
