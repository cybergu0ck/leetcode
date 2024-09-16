# 322. Coin Change

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/coin-change/description/).

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

- The question asks to find the fewest number of coins, Hence this is a optimisation problem.
- The problem has overlapping subproblems: We have to make change for the remaining amount once we use a coin.
- Therefore this is a Optimisation DP Problem, Using the DP frameork,

  #### Objective Function

  $F(i)$ is the minimum number of coins to make change for the amount $i$.

  #### Base Cases

  1. $F(0) = 0$. There is no coins needed to make change for 0.

  #### Recurrance Relation

  $F(n) = 1+F(n-j)$ if $n>=j$, for j is the coin denominations and we choose the minimum value everytime.

  - This is a recursive leap of faith, meaning we are assuming we know the answers to the previous problems.
  - We try out all the coin denominations:
    - When we choose a coin we have to count it and we need to know the minimum number of coins to make change for the remaining amount. i.e. $1 + F(n-j)$.

  #### Where to find the Answer

  The final value returned is the answer to the whole problem.

<br>

#### Recursive Solution (Top Down Approach)

```py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def rec(target):
            if target == 0:
                return 0
            minCoins = float("inf")
            for coin in coins:
                if target - coin>=0:
                    minCoins = min(minCoins, 1+rec(target - coin))
            return minCoins
        return rec(amount) if rec(amount) != float("inf") else -1
```

- This is a $O(2^n)$ solution in terms of time and $O(n)$ solution in terms of space.

<br>

#### Recursive Solution (Top Down Approach) with Memoization

```py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def rec(target):
            if target in memo:
                return memo[target]
            if target == 0:
                return 0
            minCoins = float("inf")
            for coin in coins:
                if target - coin>=0:
                    minCoins = min(minCoins, 1+rec(target - coin))
            memo[target] = minCoins
            return minCoins
        return rec(amount) if rec(amount) != float("inf") else -1
```

- This is a $O(n)$ solution in terms of time and $O(n)$ solution in terms of space.

<br>

#### Dynamic Programming Solution (Bottom Up Approach)

```py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for value in range(amount +1)] #we are considering zero as well
        dp[0] = 0 #base case
        for value in range(amount+1):
            for coin in coins:
                if value >= coin:
                    dp[value] = min(dp[value],1+dp[value-coin])

        return dp[amount] if dp[amount] != float("inf") else -1
```

- This is a $O(n)$ solution in terms of time and $O(n)$ solution in terms of space.
- I don't think the space complexity can be reduced furthur using variables as we need old answers, not just the previous ones.

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

<br>
<br>
