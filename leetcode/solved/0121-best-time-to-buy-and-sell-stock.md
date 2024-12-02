# Best Time to Buy and Sell Stock

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/).

- Some good follow ups are:
  - Can the input array be empty?

<br>
<br>

## Test Cases

| Input     | Output | Note                  |
| --------- | ------ | --------------------- |
| [1,2,3,4] | 3      | Increasing trend      |
| [4,3,2,1] | 0      | Decreasing trend      |
| [1,1,1,1] | 0      | Constant trend        |
| [1,4,3,1] | 3      | Increase and Decrease |
| [1,3,1,7] | 6      | Increae and Increase  |

<br>
<br>

## Solution

<br>

### Linear Solution

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for price in prices:
            if price > buy:
                profit = price - buy
                res = max(profit, res)
            else:
                buy = price
        return res
```

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res{0};
        int buy = prices[0];
        for(const auto& price : prices){
            if(price > buy){
                int profit = price - buy;
                res = std::max(res, profit);
            }
            else{
                buy = price;
            }
        }
        return res;
    }
};
```

- Iterate through prices, calculate and update the result if current price is greater than buy price otherwise update the buy price.
- This is a linear $O(n)$ solution in terms of time, where $n$ is the number of elements in the input array.
- This is a constant $O(1)$ solution in terms of space.

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>
<br>

## Notes

- The algorithm can be written as follows by tweaking the if and else condition little bit, I am not sure if it is better code.

  ```py
  class Solution:
      def maxProfit(self, prices: List[int]) -> int:
          res = 0
          buy = prices[0]
          for price in prices:
              if price < buy:
                  buy = price
              profit = price - buy
              res = max(profit, res)
          return res
  ```

- Python's `max()` equvivalent in C++ is `std::max()` from `algorithm` header.

<br>
<br>

## Resources

<br>
<br>
