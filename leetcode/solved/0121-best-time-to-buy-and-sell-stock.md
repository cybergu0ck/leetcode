# Best Time to Buy and Sell Stock

Easy level [question on leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)..

<br>
<br>
<br>

## Clarifications

- Can the input array be empty?

  - No

- "Shorting" is not possible right?
  - Yes, selling is done only after buying.

<br>
<br>
<br>

## Test Cases

| Case                  | Input     | Output |
| --------------------- | --------- | ------ |
| Increasing trend      | [1,2,3,4] | 3      |
| Decreasing trend      | [4,3,2,1] | 0      |
| Constant trend        | [1,1,1,1] | 0      |
| Increase and Decrease | [1,4,3,1] | 3      |
| Increae and Increase  | [1,3,1,7] | 6      |
| Edge case             | [3,1,10]  | 9      |

<br>
<br>
<br>

## Solution

<br>
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

<br>

#### Explanation

Iterate over prices, calculate and update the result if current price is greater than buy price otherwise update the buy price.

1. **One dimensionality** :

   - Since the selling can be done only after buying, Iteration must proceed in a forward direction only.

2. **Updation of buy price** :

   - During the iteration, if a price lower than the current buy price is encountered, the buy price should be updated to this new, lower value because any potential larger price ahead in the array will give the maximised profit with this lower value.

<br>

#### Complexity Analysis

- **Time Complexity**: This is a linear $O(n)$ solution in terms of time, where $n$ is the size of the input array.
- **Space Complexity**: This is a constant $O(1)$ solution in terms of space.

<br>
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
<br>

## Resources

<br>
<br>
<br>
