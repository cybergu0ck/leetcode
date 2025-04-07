# 1143. Longest Common Subsequence

Medium [level question on leetcode](https://leetcode.com/problems/longest-common-subsequence/description/).

<br>
<br>
<br>

## Clarifications

- Confirm definition of subsequence.

  - A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- Can any of the two input strings be empty?

  - `1 <= text1.length, text2.length <= 1000`

- What kind of characters are we dealing with?

  - text1 and text2 consist of only lowercase English characters.

<br>
<br>
<br>

## Test cases

| Case                                    | Input          | Output |
| --------------------------------------- | -------------- | ------ |
| Single character strings                | 'a' and 'a'    | 1      |
| All characters same                     | 'ab' and 'ab'  | 2      |
| Zero characters same                    | 'ab' and 'xy'  | 0      |
| Single character same (text1 is longer) | 'ab' and 'a'   | 1      |
| Single character same (text2 is longer) | 'a' and 'ab'   | 1      |
| Repeated character (text1 is longer)    | 'baa' and 'ab' | 2      |
| Repeated character (text2 is longer)    | 'ab' and 'aba' | 2      |

- Note that the first string is text1 and the second is text2
- The above test cases look complete.

<br>
<br>
<br>

## Solution

<br>
<br>

### Recursive solution

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

```cpp

```

<br>

#### Explanation

Use the dp framework as the question can be solved using dynamic programming:

- The problem is about finding longest common subsequence, an optimisation problem. Potentially a DP problem.
- The problem has overlapping subproblems: The subsequence of the longest common subsequence must also be common subsequence!
- Use the simplest example like 'ab','a' and 'a','ab' to come up with the objective function, base case and the recurance relation.

  #### Objective function

  $T(i,j)$ is the longest common subsequence between two strings having length i+1 and j+1 respectively (Zero based indexing is used).

  #### Base cases

  1. $T(i,j) = 0$, If either of i or j is negative. There must be atleast one character in both strings to compare.

  - Although the question specifies that either of the strings will not be empty, we still consider this base case. More obvious when we use the 2D DP grid to come up with these.

  #### Recurrance relation

  $T(i,j) = \begin{cases} 1 + T(i-1,j-1) & \text{if } \text{text1}[i] == \text{text2}[j], \\ \max(T(i-1,j), T(i,j-1)) & \text{otherwise}. \end{cases}$

  - This is a recursive leap of faith, meaning we are assuming we know the answers to the previous problems.
  - If the $i^{th}$ and $j^{th}$ characters of text1 and text2 are same then we add 1 to the previously obtained answer i.e. $T(i-1,j-1)$.
  - Otherwise we need to check two cases and pick the maximum among them:
    - Ignore the character in text1 only i.e. $T(i-1,j)$
    - Ignore the character in text2 only i.e. $T(i,j-1)$
    - We do this because text1 and text2 can be interchanged. Example : 'a','ab' and 'ab','a'.

  #### Where to find the answer

  The final value returned is the answer to the whole problem.

<br>

#### Complexity analysis

- Time Complexity : This is a exponential, $O(2^n)$ solution in terms of time, where $n$ is $\max{(len(text1), \quad len(text2))}$.
  - The time complexity is determined by the number of recursive calls which is equal to the number of nodes in the recursive tree. The maximum number of nodes for a tree with depth n and each node having two branches is $2^n$. Checkout [trees](https://github.com/cybergu0ck/notes/blob/main/engineering/software/fundamentals/data-structures/trees/01-trees.md).
  - Here the else case causes two branches and the depth of the tree can go maximum until the length of the longer text.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, This is the auxilary stack space.

<br>
<br>

### Top down dp solution

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

<br>
<br>

#### Explanation

Memoize the recursive solution using a map.

<br>
<br>

#### Complexity analysis

- Time Complexity : This is a bilinear or polynomial, $O(n*m)$ solution in terms of time, where $n$ and $m$ are the sizes of the two input strings.

  - Memoization ensures that the number of recursive calls is equal to the cells in the 2D dp grid of size $n*m$.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, This is the auxilary stack space.

<br>
<br>

### Bottom up dp solution

```py
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [ [0 for i in range(len(text2)+1)] for j in range(len(text1)+1)] #introduce padding for the base case

        #base cases are already taken care above

        for r in range(1,len(text1)+1):
            for c in range(1,len(text2)+1):
                if(text1[r-1] == text2[c-1]):   # -1 is because of the padding we have introduced
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    dp[r][c] = max(dp[r][c-1], dp[r-1][c])

        return dp[len(text1)][len(text2)]

```

<br>
<br>

#### Explanation

Tabulation using 2D DP array.

- Note that the indices play a crucial role in the above algorithm. We must start the iteration from 1st index because (index-1) is being computed.
  - While comparing the strings we need to use (index-1) to maintaing valid indexing.
  - The DP table has extra row and column the zeroth indices, for the case of empty string comparision.

<br>
<br>

#### Complexity analysis

- Time Complexity : This is a bilinear or polynomial, $O(n*m)$ solution in terms of time, where $n$ and $m$ are the sizes of the two input strings.

- Space Complexity : This is a linear, $O(n*m)$ solution in terms of space, This is the dimension of the 2d dp array.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Comming up with the correct base case is not straigh forward. Drawing the 2d array and picking up a simple test case like 'ab' and 'a' will help.

<br>
<br>
<br>

## Resources

- Watch [Back to Back SWE's video](https://www.youtube.com/watch?v=ASoaQq66foQ)
- Watch [Abdul Bari's video](https://www.youtube.com/watch?v=sSno9rV8Rhg)

<br>
<br>
<br>
