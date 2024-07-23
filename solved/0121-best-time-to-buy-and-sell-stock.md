# Best Time to Buy and Sell Stock

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://shorturl.at/Ugo4p).

<br>
<br>

## Solution

<br>

### Brute Force

- The following has $O(n^2)$ time complexity $O(1)$ space complexity, by iterating over every possible result using nested for loop.

  ```py
  ```

<br>

### Efficient Force

- The following has $O(n)$ time complexity $O(1)$ space complexity.

  ```py
  class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low = prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= low:
                cur_profit = prices[i] - low
                if cur_profit > max_profit:
                    max_profit = cur_profit
            else:
                low = prices[i]
        return max_profit
  ```

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py
  ```

<br>
<br>

## Testcases

- Early profit, something like [10,20,1,5]
- Late profit, something like [10,20,1,5,100]
- No profit, something like [10,9,8,7]

<br>
<br>

## Notes

<br>
<br>

## Resources

<br>
<br>
