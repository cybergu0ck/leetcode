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

Solving the question using Dynamic Programming as the question it poses is similar to "how many distinct ways ...", which is type of combinatorial DP questions.

- Using the DP frameork,

  1. The Objective Function, $F(i)$ is the number of ways to climb $i$ steps given one can take only 1 or 2 steps at once.
  2. The Base Case, $F(0) = 1$. There is only 1 way to climb no stairs i.e. to take no steps.
  3. The Recurrance Relation, $F(n) = F(n-1) + F(n-2)$. This is like taking a _"recursive leap of faith"_. Assuming one is $n'th$ step, he could have come from either 1 step or 2 step behind.

#### Recursive Solution

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
```

- This has exponential $O(2^n)$ time complexity $O(n)$ space complexity. The space complexity is due to the call stack for recursion.
- This recursive solution is a _"Top Down"_ Approach.

<br>

#### Dynamic Programming Solution

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        dp =[0 for stair in range(n+1)] #always of size n+1
        dp[0] = 1 #Base Case
        dp[1] = 1 #Extra Base case needed for the following dp iteration
        for stair in range(2,n+1):
            dp[stair] = dp[stair-1] + dp[stair-2]
        return dp[n]
```

- This linear $O(n)$ time complexity $O(n)$ space complexity.
- This is "_Bottom Up_" Approach using tabulation, true DP solution.
- **Note that we need an extra base case here. If we use only one base case then it'll cause an issue in the first iteration as dp[stair-2] will be an out of index operation!**

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
