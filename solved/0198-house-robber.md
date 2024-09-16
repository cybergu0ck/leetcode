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

- The question asks us to find the maximum amount, Hence this is an Optimisation question.
- The problem has overlapping subproblems: If we rob the n'th house then we can add the n'th house amount to the amount obtained from robbing (n-2)th house. (This is not the recurrance relation, This is just hinting about the subproblem).
- Therefore this is a Optimisation DP Problem. Using the DP frameork,

  #### Objective Function

  $F(i)$ is the maximum amount robbed given considering all the houses till index "$i$".

  #### Base Cases

  1. $F(0) = nums[0]$. There's only 1 house to rob, we just rob it.
  2. $F(1) = max(nums[0], nums[1])$. If there are 2 houses, it means we can rob either of one. We rob the wealhier one.

  #### Recurrance Relation

  $F(n) = max(nums[n] + F(n-2), F(n-1))$

  - This is a recursive leap of faith, meaning we are assuming we know the answers to the previous problems.
  - We can choose to rob the $n'th$ house, Then we have to add the $n'th$ house's wealth to whatever we get from robbing $(n-2)'th$ house. We can choose not to rob the $n'th$ house and consider the amount got from robbing $(n-1)'th$ house. We have to choose the maximum between these 2 options.

  #### Where to find the Answer

  The final value returned is the answer to the whole problem.

<br>

#### Recursive Solution (Top Down Approach)

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rec(index):
            if index == 0:
                return nums[0]
            if index == 1:
                return max(nums[0], nums[1])
            return max(nums[index] + rec(index-2), rec(index-1))
        return rec(len(nums)-1)
```

- This is a linear $O(2^n)$ solution in terms of time and linear $O(n)$ solution in terms of space.

<br>

#### Recursive Solution (Top Down Approach) with Memoization

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def rec(index):
            if index in memo:
                return memo[index]
            if index == 0:
                return nums[0]
            if index == 1:
                return max(nums[0], nums[1])
            memo[index] = max(nums[index] + rec(index-2), rec(index-1))
            return memo[index]
        return rec(len(nums)-1)
```

- This is a linear $O(n)$ solution in terms of time and linear $O(n)$ solution in terms of space.

<br>

#### Dynamic Programming Solution (Bottom Up Approach)

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0 for num in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[len(nums)-1]
```

- This is a linear $O(n)$ solution in terms of time and linear $O(n)$ solution in terms of space.

<br>

#### Dynamic Programming Solution (Bottom Up Approach) with Space Optimization

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prevToPrev = nums[0]
        prev = max(nums[0], nums[1])

        for house in range(2,len(nums)):
            robbing = max(nums[house]+prevToPrev, prev)
            prevToPrev = prev
            prev = robbing

        return prev
```

- This is a linear $O(n)$ solution in terms of time and linear $O(1)$ solution in terms of space.

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

- This is a "less code" version of the above problem, which is more intuitive in my opinion.
- This is a linear $O(n)$ solution in terms of time and linear $O(1)$ solution in terms of space.

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

```
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rec(index):
            if index == 0:
                return nums[0]
            if index == 1:
                return max(nums[0], nums[1])
            return max(nums[index] + rec(index-2), rec(index-1))
        return rec(len(nums)-1)
```
