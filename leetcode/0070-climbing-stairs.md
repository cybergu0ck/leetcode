# 70. Climbing Stairs

Easy [level question on leetcode](https://leetcode.com/problems/climbing-stairs/description/).

<br>
<br>
<br>

## Clarifications

- Can n be zero? meaning no step needs to be climbed?
  - 1 <= n <= 45

<br>
<br>
<br>

## Test cases

| Case | Input | Output |
| ---- | ----- | ------ |
|      | 1     | 1      |
|      | 2     | 2      |
|      | 3     | 3      |

<br>
<br>
<br>

## Solution

<br>
<br>

### Recursive solution

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==0 or n==1):
            return 1
        return self.climbStairs(n-1)+ self.climbStairs(n-2)
```

```cpp

```

<br>

#### Explanation

Use the framework for solving recusrive question

- The question asks to find the number of distinct ways, a combinatorial problem. Potentially a DP problem.
- The problem has overlapping subproblems: If we are on the n'th stair, then the number of ways to have climbed that stair is basically the number of ways to climb (n-1)'th stair and number of ways to climb (n-2)th stair. (This in itself is the recurrance relation.)

1.  Define the objective function.

    $F(i)$ is the number of ways to have climbed $i'th$ stair given one can take only 1 or 2 steps at once.

2.  Identify the base cases.

    - $F(0) = 1$. There is only 1 way to climb no stairs i.e. to take no steps.
    - $F(1) = 1$. There is only 1 way to climb no stairs i.e. to take 1 step.

3.  Form the recurrance relation.

    $F(n) = F(n-1) + F(n-2)$

    - This is a recursive leap of faith, meaning we are assuming we know the answers to the previous problems.
    - Assuming one is $n'th$ step, he could have come from either 1 step or 2 step behind.

4.  Find the answer.

    The final value returned is the answer to the whole problem.

<br>

#### Complexity analysis

- Time Complexity : This is a exponential, $O(2^n)$ solution in terms of time, where $n$ is number of stairs.

  - The time complexity is determined from the number of recursive calls made. Drawing a recursive tree will shows that the height of the tree is $n-1$ and the number of nodes will be equal to $2^{n-1}-1$. The number of nodes is essentially the number of times the recursive function is called. Hence the time complexity is exponential i.e. $O(2^n)$.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is number of stairs.

  - The space complexity is determined by the maximum depth of the recursive call stack. Drawing a recursive tree shows that the height of the tree is $n-1$, The height of the tree is essentially the depth of the recursive call stack.

<br>
<br>

### Top down dp solution

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climbStairsMemo(n):
            if(n in memo):
                return memo[n]
            if(n==0 or n==1):
                return 1
            res = climbStairsMemo(n-1)+ climbStairsMemo(n-2)
            memo[n] = res
            return res
        return climbStairsMemo(n)
```

```cpp

```

<br>

#### Explanation

Use a hash map to cache the results.

- The core logic is same as that of [recursive solution](#recursive-solution)

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of stairs.

  - Each value of n is calculated only once dues to memoization.

- Space Complexity : This is a llinear, $O(n)$ solution in terms of space, where $n$ is the number of stairs.

  - The space used by memo map is proportional to $n$. Also the recursive call stack consumes linear space, anyway overall it is linear.

<br>
<br>

### Bottom up dp solution

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1 for i in range(n+1)]

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
```

```cpp

```

<br>

#### Explanation

Use 1D array and recurrance relation to code the bottom up dp approach.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of stairs.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the number of stairs.
- Although the time and space complexity seems same as that of [top down apprach](#top-down-dp-solution), this bottom up approach is better as it avoids recursion.

<br>
<br>

### Bottom up dp solution with space optimisation

```py
class Solution:
    def climbStairs(self, n: int) -> int:
        one_step_before = 1
        two_step_before = 1

        for i in range(2,n+1):
            cur = one_step_before + two_step_before
            two_step_before = one_step_before
            one_step_before = cur

        return one_step_before
```

```cpp

```

<br>

#### Explanation

Use variables and recurrance relation to code the bottom up dp approach.

- This is the best solution for this question

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of stairs.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

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
