# 1143. Longest Common Subsequence

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/longest-common-subsequence/description/).

- Some good follow ups are:

<br>
<br>

## Solution

<br>

### Brute Force

```py

```

- This is a $O()$ solution in terms of time and $O()$ solution in terms of space.

<br>

### Efficient Solution

- The question asks us to find the longest value, Hence this is an optimisation question.
- The problem has overlapping subproblems: The subsequence of a longest common subsequence must also be common subsequence.
- Therefore this is a Optimisation DP Problem. Using the DP frameork,

  #### Objective Function

  $F(i,j)$ is longest increasing sequence between two strings having length (i+1) and (j+1) respectively.

  #### Base Cases

  1. $F(i,j) = 0$ if either of i or j is negative. There must be atleast one character in both strings to compare commanality.

  #### Recurrance Relation

  $F(i,j) = 1+F(i-1,j-1)$ if $text1[i]$ < $text2[j]$ else $max(F(i-1,j), F(i,j-1))$.

  - This is taking a recursive leap of faith. Assuming we know the answer to the subproblem.
  - If the characters are common then we add 1 to the subproblem of finding the longest common subsequence of the remaining strings. i.e. We chop off the common character.
  - If the characters are not common, we have two options:
    - We can ignore the character in the first string and compare the rest.
    - We can ignore the character in the second string and compare the rest.
    - We have to choose the one which gives the maximum value.

  #### Where to find the Answer

  The final value returned is the answer to the whole problem.

<br>

#### Recursive Solution (Top Down Approach)

```py
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def rec(i,j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return 1 + rec(i-1, j-1)
            else:
                return max(rec(i-1,j), rec(i,j-1))

        return rec(len(text1)-1, len(text2)-1)
```

- This is a exponential $O(2^min(len(text1),len(text2)))$ solution in terms of time and linear $O(min(len(text1),len(text2)))$ solution in terms of space.
  - Minimum value is considered for time complexity because the recursion ends when one of the index becomes negative and the text with the smaller length will end the recursion depth.
  - The space complexity is due to recursive stack.

<br>

#### Recursive Solution (Top Down Approach) with Memoization

```py
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def rec(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + rec(i-1, j-1)
                return memo[(i,j)]
            else:
                memo[(i,j)] = max(rec(i-1,j), rec(i,j-1))
                return memo[(i,j)]

        return rec(len(text1)-1, len(text2)-1)
```

- This is a quadratic $O(len(text1) * len(text2))$ solution in terms of time and linear $O(len(text1) + len(text2))$ solution in terms of space.

<br>

#### Dynamic Programming Solution (Bottom Up Approach)

```py
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]    #considering zeroth indices as base cases when the strings are empty, this is the base case itself.

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1)][len(text2)]

```

- Note that the indices play a crucial role in the above algorithm. We must start the iteration from 1st index because (index-1) is being computed.
  - While comparing the strings we need to use (index-1) to maintaing valid indexing.
  - The DP table has extra row and column the zeroth indices, for the case of empty string comparision.
- This is a quadratic $O(len(text1) * len(text2))$ solution in terms of time and quadratic $O(len(text1) * len(text2))$ solution in terms of space.
  - The space complexity is because of the 2D DP table.

<br>

### Ideal Solution

```py

```

- This is a $O()$ solution in terms of time and $O()$ solution in terms of space.

<br>
<br>

## Notes

<br>
<br>

## Test Cases

<br>
<br>

## Resources

- Watch [Back to Back SWE's video](https://www.youtube.com/watch?v=ASoaQq66foQ)
- Watch [Abdul Bari's video](https://www.youtube.com/watch?v=sSno9rV8Rhg)

<br>
<br>
