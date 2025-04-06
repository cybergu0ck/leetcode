# 123. Best Time to Buy and Sell Stock III

Hard [level question on leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/).

<br>
<br>
<br>

## Clarifications

<br>
<br>
<br>

## Test cases

In all the cases the number of transactions allowed is two.

| Case | Input             | Output |
| ---- | ----------------- | ------ |
|      | [3,3,5,0,0,3,1,4] | 6      |
|      | [1,2,3,4,5]       | 4      |
|      | [7,6,4,3,1]       | 0      |

<br>
<br>
<br>

## Solution

<br>
<br>

### Recursive solution

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def maxProfitRec(i, j):
            if(i == 0 or j == 0):
                return 0
            not_sell_case = maxProfitRec(i, j-1)
            sell_case = 0
            for b in range(j-1):
                profit = prices[j-1] - prices[b] + maxProfitRec(i-1, b)
                if(profit > sell_case):
                    sell_case = profit
            return max(not_sell_case, sell_case)
        return maxProfitRec(2, len(prices))

```

```cpp

```

<br>

#### Explanation

Use the framework for solving recusrive question.

- The question asks to find the maximum profit, an optimisation problem. Potentially a DP problem.
- The problem has overlapping subproblems: Any given day, we can either choose to sell the stock (given we have bought it) otherwise we consider maximum profit until previous day.

1.  Define the objective function.

    $F(i,j)$ is the maximum profit considering $i$ number of transactions (sell after a buy) until $j'th$ day.

2.  Identify the base cases.

    - $F(i,j) = 0$ for all i = 0. No profit can be made if there is 0 transactions.
    - $F(i,j) = 0$ for all j = 0. No profit can be made on the first day itself.

3.  Form the recurrance relation.

    $F(i,j) = \max(F(i, j-1), \max(\quad \text{prices}[j] - \text{prices}[b] + F(i-1, b) \quad \text{for all } b \text{ from } 0 \text{ to } j-1))$

    - On a given day, if we consider not to sell then the maximum profit of the previous day considering the same number of transactions will continue as the maximum profit i.e. $F(i, j-1)$.
    - On a given day, if we consider to sell, then we have to select the maximum of all the computions of profits considering all the days before as buy day's i.e. $\text{prices}[j] - \text{prices}[b]$ and for every computation we must add the maximum profit considering one less transaction for that buy day i.e. $F(i-1, b)$
    - Since we have to maximise the profit, we select the maximum of the above two choices.

4.  Find the answer.

    The final value returned is the answer to the whole problem.

<br>

#### Complexity analysis

- Time Complexity : This is exponential, $O(k^n)$ solution in terms of time. Here $k$ is the number of days and $n$ is the number of transactions allowed.
  - Not exactly sure about the above mathematical expression.
  - In the worst case, the number of branches in the recursion tree will be the number of days in the given input array and the depth of the tree will be the number of transactions allowed.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space. This is auxilary stack space.

<br>
<br>

### Top down dp solution

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def maxProfitRec(i, j):
            if(i == 0 or j == 0):
                return 0
            not_sell_case = maxProfitRec(i, j-1)
            sell_case = 0
            for b in range(j-1):
                profit = prices[j-1] - prices[b] + maxProfitRec(i-1, b)
                if(profit > sell_case):
                    sell_case = profit
            res = max(not_sell_case, sell_case)
            memo[j] = res
            return res
        maxProfitRec(2, len(prices))
        return memo[len(prices)]
```

<br>

#### Explanation

Memoize the recursive solution using a map.

<br>

#### Complexity analysis

- Time Complexity : This is a bilinear or polynomial, $O(n*m)$ solution in terms of time, where $n$ is the number of allowed transactions and $m$ is the number of days.

  - Basically the recursion is accounted once for each cell in the 2D DP array (n \* m).

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the auxilary stack space.

<br>
<br>

### Bottom up dp solution

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_transactions = 2
        dp = [ [0 for j in range(len(prices))] for transaction in range(max_transactions+1)] #base cases are covered here

        for i in range(1,max_transactions+1):
            for j in range(1,len(prices)):
                profit = 0
                for b in range(j):
                    cur = prices[j]-prices[b] + dp[i-1][b]
                    if(cur > profit):
                        profit = cur
                dp[i][j] = max(dp[i][j-1], profit)
        print(dp)
        return dp[-1][-1]
```

<br>

#### Explanation

<br>

#### Complexity analysis

- Time Complexity : This is a bilinear or polynomial, $O(n*m)$ solution in terms of time, where $n$ is the number of allowed transactions and $m$ is the number of days.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the size of the dp array.

<br>
<br>

### Bottom up dp solution with optimisation

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_transactions = 2
        dp = [ [0 for j in range(len(prices))] for transaction in range(max_transactions+1)] #base cases are covered here

        for i in range(1,max_transactions+1):
            comp = -prices[0]  #This initialisation is crucial
            for j in range(1,len(prices)):
                comp = max(comp, -prices[j-1] + dp[i-1][j-1])
                dp[i][j] = max(dp[i][j-1], prices[j]+comp)
        print(dp)
        return dp[-1][-1]
```

<br>

#### Explanation

Avoid redundanct calculations.

<br>

#### Complexity analysis

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- The final optimised DP solution is non-intuitive.

<br>
<br>
<br>

## Resources

- The DP solution is from [Keerthi puruswani](https://www.youtube.com/watch?v=2FROyvnnrrM)

<br>
<br>
<br>
