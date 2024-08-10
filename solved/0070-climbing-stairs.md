# 70. Climbing Stairs

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/climbing-stairs/description/).

- Some good follow ups are:

<br>
<br>

## Solution

<br>

### Brute Force

```py

```

- The following has $O()$ time complexity $O()$ space complexity.

<br>

### Efficient Solution

- The question asks to find the number of ways, Hence this is a combinatorial problem.
- The problem has overlapping subproblems: If we are on the n'th stair, then the number of ways to have climbed that stair is basically the number of ways to climb (n-1)'th stair and number of ways to climb (n-2)th stair. (This in itself is the recurrance relation.)
- Therefore this is a Combinatorial DP Problem, Using the DP frameork,

  #### Objective Function

  $F(i)$ is the number of ways to have climbed $i'th$ stair given one can take only 1 or 2 steps at once.

  #### Base Cases

  1. $F(0) = 1$. There is only 1 way to climb no stairs i.e. to take no steps.

  #### Recurrance Relation

  $F(n) = F(n-1) + F(n-2)$.

  - This is a recursive leap of faith, meaning we are assuming we know the answers to the previous problems.
  - Assuming one is $n'th$ step, he could have come from either 1 step or 2 step behind.

  #### Where to find the Answer

  The final value returned is the answer to the whole problem.

<br>

#### Recursive Solution (Top Down Approach)

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(n):
            if n == 0 or n == 1:
                return 1
            return rec(n-1) + rec(n-2)
        return rec(n)
```

- This has exponential $O(2^n)$ time complexity $O(n)$ space complexity. The space complexity is due to the call stack for recursion.

<br>

#### Recursive Solution (Top Down Approach) with Memoization

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def rec(n):
            if n in memo:
                return memo[n]
            if n == 0 or n == 1:
                return 1
            memo[n] = rec(n-1) + rec(n-2)
            return memo[n]
        return rec(n)
```

- This has exponential $O(n)$ time complexity $O(n)$ space complexity.

<br>

#### Dynamic Programming Solution (Bottom Up Approach)

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        dp =[0 for stair in range(n+1)] #We are also considering the zeroth stair
        dp[0] = 1 #Base Case
        dp[1] = 1 #Extra Base case needed for the following dp iteration
        for stair in range(2,n+1):
            dp[stair] = dp[stair-1] + dp[stair-2]
        return dp[n]
```

- This is linear $O(n)$ time complexity and linear $O(n)$ space complexity.
- This is "_Bottom Up_" Approach using tabulation, true DP solution.
- **Note that we need an extra base case here. If we use only one base case then it'll cause an issue in the first iteration as dp[stair-2] will be an out of index operation!**

<br>

#### Dynamic Programming Solution (Bottom Up Approach) with Space Optimization

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        prevToPrev = 1
        prev = 1
        for i in range(2,n+1):
            cur = prev + prevToPrev
            prevToPrev = prev
            prev = cur
        return prev
```

- This is linear $O(n)$ time complexity and constant $O(1)$ space complexity.

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
