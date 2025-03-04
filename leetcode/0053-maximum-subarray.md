# Maximum Subarray

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/maximum-subarray/description/).

- Some good follow ups are:
  - Checkout the meaning of subarray down in notes section.

<br>
<br>

## Test Cases

| Input           | Output | Note                                   |
| --------------- | ------ | -------------------------------------- |
| [1,2,3,0]       |        | All positive numbers (includes a zero) |
| [-1,-2,-3]      | 0      | All negative numbers                   |
| [1,2,-1,3,-5,7] |        | Mix of positive and negative numbers   |

<br>
<br>

## Solution

<br>

### Brute Force

```py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                cur_sum = 0
                for k in range(i,j+1):
                    cur_sum += nums[k]
                    res = max(res, cur_sum)
        return res
```

- This is a cubic $O(n^3)$ solution in terms of time, where $n$ is the size of the input array.
- This is a constant $O(1)$ solution in terms of space.

<br>

### Quadratic Solution

```py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                res = max(res, cur_sum)
        return res
```

- Getting rid of the inner most for loop and using the variable to keep track of the sum directly.
- This is a quadratic $O(n^2)$ solution in terms of time, where $n$ is size of the input array.
- This is a constant $O(1)$ solution in terms of space.

<br>
<br>

### Linear Solution

```py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = float('-inf')
        max_ending_here = 0
        for num in nums:
            max_ending_here += num
            max_so_far = max(max_so_far, max_ending_here)
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far
```

```cpp
#include <limits.h>
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_so_far = INT_MIN;
        int max_ending_here{0};
        for(int num : nums){
            max_ending_here += num;
            max_so_far = std::max(max_so_far, max_ending_here);
            if(max_ending_here < 0)
                max_ending_here = 0;
        }
        return max_so_far;
    }
};
```

- Utilise Kadane's Algorithm.
  - Kadane's algorithm is a DP technique.
  - While iterating over the array, calculate the max_ending_here and carry it for future iterations only if it is positive else reset it to zero, update the max_so_far variable in each iteration.
- This is a linear $O(n)$ solution in terms of time, where $n$ is size of the input array.
- This is a constant $O(1)$ solution in terms of space.

<br>
<br>

## Notes

- A subarray is a contiguous non-empty sequence of elements within an array.
- Include `#include<limits.h>` to include `INT_MIN` .
  <br>
  <br>

## Resources

- [This](https://www.youtube.com/watch?v=AHZpyENo7k4) video explains kadane's algorithm flawlessly.

<br>
<br>
