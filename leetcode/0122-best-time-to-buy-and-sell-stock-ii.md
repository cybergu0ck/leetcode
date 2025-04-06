# 122. Best Time to Buy and Sell Stock II

Medium [level question on leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/).

<br>
<br>
<br>

## Clarifications

- What is the expected output if the input array is empty?

  - $1 <= prices.length <= 3 * 10^4$

- It is common knowledge that the prices cannot be negative right?

  - $0 <= prices[i] <= 10^4$

<br>
<br>
<br>

## Test cases

| Case                   | Input         | Output |
| ---------------------- | ------------- | ------ |
| random                 | [7,1,5,3,6,4] | 7      |
| continously increasing | [1,2,3,4,5]   | 4      |
| continously decreasing | [7,6,4,3,1]   | 0      |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        buy = 0

        for i in range(1, len(prices)):
            if prices[i] <= prices[buy]:
                buy = i
            else:
                profit = prices[i] - prices[buy]
                profits += profit
                buy = i

        return profits
```

```cpp

```

<br>

#### Explanation

Intuitive approach. On any given day if the price is high than the buy price, take the profit and buy on that day again. If the price is low then update the buy price.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is size of the input array.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- The generalised solution from [leetcode 123](./0123-best-time-to-buy-and-sell-stock-iii.md) can be used, however is not better than the above brute force solution in terms of time, I believe.

  ```
  class Solution:
      def maxProfit(self, prices: List[int]) -> int:
          max_transactions = len(prices)-1 #tweaked for this question
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
<br>
<br>

## Resources

<br>
<br>
<br>
