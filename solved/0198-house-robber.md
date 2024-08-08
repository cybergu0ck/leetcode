# 198. House Robber

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/house-robber/description/).

- Some good follow ups are:

<br>
<br>

## Solution

<br>

### Brute Force

```py

```

- The following has $O()$ time complexity $O()$ space complexity.

<br>

### Efficient Solution

Solving the question using Dynamic Programming as the question it poses is similar to "maximise the ...", which is type of optimization DP questions.

- Using the DP frameork,

  1. The Objective Function, $F(nums[])$ is the maximum amount robbed given the array nums.
  2. The Base Case, $F(nums[]) = 0$ when size of array nums is 0. No amount can be robbed if there are no houses.
  3. The Recurrance Relation, $F(nums[]) = max(nums[0] + F(nums[2::]), F(nums[1::]))$. There is two options, either we can choose to rob first house then we have to continue the robbing process from the third house onwards i.e. skipping second house or we can choose to skip the first house and continue the robbing process from second house. Ofcourse, the best option is the one where the robbing is maximised.

#### Recursive Solution

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        return max(nums[0] + self.rob(nums[2::]), self.rob(nums[1::]))
```

- The following has $O(2^n)$ time complexity $O(n)$ space complexity. The space complexity is due to the call stack for recursion.
- This recursive solution is a _"Top Down"_ Approach.

<br>

#### Dynamic Programming Solution

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0 for num in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[len(nums)-1]
```

- The following has $O(n)$ time complexity $O(n)$ space complexity.

<br>

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for num in nums:
           current = max(num + rob1, rob2)
           rob1 = rob2
           rob2 = current

        return rob2
```

- The following has $O(n)$ time complexity $O(1)$ space complexity.
- This DP solution is a _"Bottom Up"_ Approach.

<br>

### Ideal Solution

```py

```

- The following has $O()$ time complexity $O()$ space complexity.

<br>
<br>

## Notes

<br>
<br>

## Test Cases

1. Empty Array: []
2. One house only: [1]
3. Two house only: [1,3]
4. Three house only: [1,3,1]
5. Lot of houses: [1,2,3,1]

<br>
<br>

## Resources

- Watch neetcode's explanation.

<br>
<br>
