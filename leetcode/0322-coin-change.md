# 322. Coin Change

Medium [level question on leetcode](https://leetcode.com/problems/coin-change/description/).

<br>
<br>
<br>

## Clarifications

- Can the input array be empty?

  - `1 <= coins.length <= 12`

- Is is obvious to assume that all the integers in the input array are positive and non-zero?

  - `1 <= coins[i] <= 2^31 - 1`

- Can the amount be zero?

  - `0 <= amount <= 104`

<br>
<br>
<br>

## Test cases

| Case | Input                        | Output |
| ---- | ---------------------------- | ------ |
|      | coins = [1], amount = 1      | 1      |
|      | coins = [1], amount = 0      | 0      |
|      | coins = [1], amount = 2      | -1     |
|      | coins = [1,2,5], amount = 11 | 3      |
|      | coins = [1,2,5], amount = 11 | 3      |

<br>
<br>
<br>

## Solution

<br>
<br>

### Recursive solution

```py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def rec(target):
            if target == 0:
                return 0
            min_coins = float("inf")
            for coin in coins:
                if(target - coin >=0):
                    min_coins = min(min_coins, 1+rec(target - coin))
            return min_coins
        return rec(amount) if rec(amount) != float("inf") else -1
```

```cpp

```

<br>

#### Explanation

Use the dp framework as the question can be solved using dynamic programming:

- The problem is about finding minimum number of coins, an optimisation problem. Potentially a DP problem.
- The problem has overlapping subproblems: Once a coin is used to make change, change must be made for the remaining amount.

  #### Objective function

  $T(n)$ is the minimum number of coins to make change for the amount $n$.

  #### Base cases

  1. $T(0) = 0$. There is no coins needed to make change for 0.

  #### Recurrance relation

  $T(n) = 1  + \min(T(n-c_1), T(n-c_2), T(n-c_3),..., T(n-c_k))   \quad \text{where c\_k is the coin at kth index in coins}$

  - This is a recursive leap of faith, meaning we are assuming we know the answers to the previous problems.
  - Try each denomination of the coin. Once a coin has been chosen, it must be counted to find out how many coins are required to make change for the remaining amount.

  #### Where to find the answer

  The final value returned is the answer to the whole problem.

<br>

#### Complexity analysis

- Time Complexity : This is a exponential, $O(k^n)$ solution in terms of time, where $k$ is the number of coin denominations and $n$ is the amount for which change has to be made.

  - For every recursive call, subsequently $k$ number of calls are made (among which the minimum is chosen). The depth of the recursive tree will be $n$ in the worst case, where the coin denomination is 1. Hence the number of nodes for such a tree where the depth is $n$ and each node branches out $k$ times is of the order $k^n$. See notes about [trees](https://github.com/cybergu0ck/notes/blob/main/engineering/software/fundamentals/data-structures/trees/01-trees.md).

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the auxilary stack space.

<br>
<br>

### Top down dp solution

```py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        def rec(target):
            if(target in mem):
                return mem[target]
            if(target == 0):
                return 0
            min_coins = flaoat("inf")
            for coin in coins:
                if(target - coin >=0):
                    min_coins = min(min_coins, 1+rec(target - coin))
            mem[target] = min_coins
            return min_coins
        return rec(amount) if rec(amount) != float("inf") else -1
```

<br>

#### Explanation

Memoize the recursive solution using a map.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the amount to make change for.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the auxilary stack space.

<br>
<br>

### Bottom up dp solution

```py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if(i-coin >= 0):
                    dp[i] = min(dp[i], 1 + dp[i-coin])

        return dp[amount] if dp[amount] != float('inf') else -1
```

<br>

#### Explanation

Use tabulation.

<br>

#### Complexity analysis

- Time Complexity : This is a psuedo-polynomial, $O(n*k)$ solution in terms of time, where $n$ is the amount to make change for and $k$ is the number of coin denominations.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is space occupied by dp array.

<br>
<br>
<br>

## Follow ups

- Is it correct that the memoized solution is better in terms of time complexity than the tabulated solution?

<br>
<br>
<br>

## Notes

- Keep revisiting this question as the implementation of the recursive solution is not exactly intuitive, specifically we donot handle the case for negative input values for the recursive function perhaps in the base case. So in the implementaion we manually avoid such calls.

<br>
<br>
<br>

## Resources

- Watch [neetcode](https://www.youtube.com/watch?v=H9bfqozjoqshttps://www.youtube.com/watch?v=H9bfqozjoqs) explanation about why a greedy approach cannot be used to solve this question.

<br>
<br>
<br>
