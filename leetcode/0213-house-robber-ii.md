# 213. House Robber II

Medium [level question on leetcode](https://leetcode.com/problems/house-robber-ii/description/).

<br>
<br>
<br>

## Clarifications

The following contraints should answer for clarifications

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

<br>
<br>
<br>

## Test cases

| Case | Input     | Output |
| ---- | --------- | ------ |
|      | [1]       | 1      |
|      | [1,2]     | 2      |
|      | [2,3,2]   | 3      |
|      | [1,2,3,1] | 4      |

- The above test cases looks complete for the given question.

<br>
<br>
<br>

## Solution

<br>
<br>

### Bottom up dp solution

```py
class Solution:
    def rob1(self,nums):
        rob1, rob2 = 0,0
        for num in nums:
            cur = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = cur
        return rob2

    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.rob1(nums[:-1]),self.rob1(nums[1:]))
```

```cpp

```

<br>

#### Explanation

Run the house robber algorithm twice, once excluding the first house and then the last house and return the maximum.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of houses or the size of the input array.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Checkout [leetcode 198, house robber](./0198-house-robber.md)

<br>
<br>
<br>

## Resources

- Got this clever approach from neetcode.

<br>
<br>
<br>
