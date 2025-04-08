# 62. Unique Paths

Medium [level question on leetcode](https://leetcode.com/problems/unique-paths/description/).

<br>
<br>
<br>

## Clarifications

- The following contraint should clarify.

  - `1 <= m, n <= 100`

<br>
<br>
<br>

## Test cases

| Case | Input        | Output |
| ---- | ------------ | ------ |
|      | m = 3, n = 2 | 3      |

- Not really driven by test cases.

<br>
<br>
<br>

## Solution

<br>
<br>

### Recursive solution

```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def rec(i,j):
            if(i < 0 or j < 0):
                return 0
            elif(i == 0 and j == 0):
                return 1
            return rec(i-1,j) + rec(i, j-1)

        return rec(m-1, n-1)
```

```cpp

```

<br>

#### Explanation

Use the framework for solving recusrive question

- The question asks to find the number of unique ways, a combinatorial problem. Potentially a DP problem.
- The problem has overlapping subproblems: Given a cell say (i,j) the number of ways to arrive to that cell noting only down and right movement is allowed is basically the number of ways to arrive at cell (i-1,j) and cell (i,j-1).

1.  Define the objective function.

    $T(i,j)$ is the number of unique ways to end up in cell (i,j) by taking only down and right movements.

2.  Identify the base cases.

    - $T(i,j) = 0 \quad \text{for either i < 0 or j < 0}$.
    - $T(0,0) = 1$. There is only 1 way to arrive at cell (0,0). By taking no movements.

3.  Form the recurrance relation.

    $T(m,n) = T(m-1, n) + T(m, n-1)$

    - This is a recursive leap of faith, meaning we are assuming we know the answers to the previous problems.
    - Assuming one is at cell (m,n), the ways one could arrive there is only from top and left (as only down and right movements are allowed) and hence the number of ways of arriving at cell (m,n) is by adding the number of ways to get to those two options.

4.  Find the answer.

    The final value returned is the answer to the whole problem.

<br>

#### Complexity analysis

- Time Complexity : This is a exponential, $O(2^{max(m,n)})$ solution in terms of time, where $m$ and $n$ are the given inputs.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space. This is the auxilary stack space.

<br>
<br>

### Top down dp solution

```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}
        def rec(i,j):
            if((i,j) in mem):
                return mem[(i,j)]
            elif(i < 0 or j < 0):
                return 0
            elif(i == 0 and j == 0):
                return 1
            mem[(i,j)] = rec(i-1,j) + rec(i, j-1)
            return rec(i-1,j) + rec(i, j-1)

        return rec(m-1, n-1)
```

```cpp

```

<br>

#### Explanation

Memoize using a map.

<br>

#### Complexity analysis

- Time Complexity : This is a bi-linear, $O(m*n)$ solution in terms of time, where $m$ and $n$ are the given inputs.

  - Recursive calls are reduced to 1 for each cell in the given grid.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the size of the map.

  - The space used by memo map is proportional to $n$. Also the recursive call stack consumes linear space, anyway overall it is linear.

<br>
<br>

### Bottom up dp solution

```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [0 for i in range(n+1)] for j in range(m+1)]
        dp[1][1] = 1

        for r in range(1, m+1):
            for c in range(1, n+1):
                if(r == 1 and c == 1):
                    continue
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[m][n]
```

```cpp

```

<br>

#### Explanation

Use tabulation using 2D dp array.

- Additional padding for top and left side of the 2D dp array is to be introduced with base case values of 0.
- It is not easy to account for the edge case of incluing the if condition while implementing the algorithm. This is because of the padding introduced and the way the nested for loops iterate over the cells essentially.

<br>

#### Complexity analysis

- Time Complexity : This is a bi-linear, $O(m*n)$ solution in terms of time, where $m$ and $n$ are the given inputs.
- Space Complexity : This is a bi-linear, $O(m*n)$ solution in terms of space. This is the size of the 2D dp array.

<br>
<br>
<br>

## Follow ups

- Optimise the space complexity further using variables or 1D arrays instead of 2D array! <!-- TODO  -->
- What if diagonal movements were allowed?

<br>
<br>
<br>

## Notes

- There is a edge case (if condition) in the implementation of [bottom up dp solution](#bottom-up-dp-solution).

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
