# 198. House Robber

Medium [level question on leetcode](https://leetcode.com/problems/house-robber/description/).

<br>
<br>
<br>

## Clarifications

- Can the input array be empty?

  - `1 <= nums.length <= 100`

- What is the elements of the input array like? Can it be negative?
  - `0 <= nums[i] <= 400`

<br>
<br>
<br>

## Test cases

| Case          | Input     | Output |
| ------------- | --------- | ------ |
| Single house  | [1]       | 1      |
| Couple houses | [1,2]     | 2      |
| Many houses   | [1,2,3,1] | 4      |

- The above test cases look complete.

<br>
<br>
<br>

## Solution

<br>
<br>

### Recursive solution

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rec(index):
            if index == 0:
                return nums[0]
            if index == 1:
                return max(nums[0], nums[1])
            return max(rec(index-1), nums[index] + rec(index-2))
        return rec(len(nums)-1)
```

```cpp

```

<br>

#### Explanation

Use the dp framework as the question can be solved using dynamic programming:

- The problem is about finding maximum amount of money, an optimisation problem. Potentially a DP problem.
- The problem has overlapping subproblems: At any given house we can choose to either rob or not rob. If we choose not to rob, then the maximum amount will be whatever was previous and if choose to rob then the maximum amount will be the amount at the current house plus the maximum amount considering two houses prior to the current one.

  #### Objective function

  $T(n)$ is the maximum amount robbed considering all the houses until index $n$.

  #### Base cases

  1. $T(0) = nums[0]$. Rob the only house that is present.
  1. $T(1) = max(nums[0], nums[1])$. In the case of two houses, rob the wealthier house.

  #### Recurrance relation

  $T(n) = max(T(n-1), \quad nums[n] + T(n-2))$

  - This is a recursive leap of faith, meaning we are assuming we know the answers to the previous problems.
  - If the $n$th house is robbed, the wealth of the $n$th house is added to the maximum amount obtained from robbing the $(n-2)$th house. Alternatively, if the $n$th house is not robbed, the maximum amount is taken from robbing the $(n-1)$th house. The optimal solution is determined by selecting the maximum value between these two options.

  #### Where to find the answer

  The final value returned is the answer to the whole problem.

<br>

#### Complexity analysis

- Time Complexity : This is a exponential, $O(2^n)$ solution in terms of time, where $n$ is the number of houses or the size of the input array.

  - The time complexity is determined by the number of recursive calls which is equal to the number of nodes in the recursive tree. The maximum number of nodes for a tree with depth n and each node having two branches is $2^n$. Checkout [trees](https://github.com/cybergu0ck/notes/blob/main/engineering/software/fundamentals/data-structures/trees/01-trees.md).

- Space Complexity : This is a linear, $O(n)$ solution in terms of space. This is the auxilary stack space.

<br>
<br>

### Top down dp solution

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
            memo[index] = max(rec(index-1), nums[index] + rec(index-2))
            return memo[index]
        return rec(len(nums)-1)
```

<br>

#### Explanation

Memoize the recursive solution using a map.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of houses or the size of the input array.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the auxilary stack space.

<br>
<br>

### Bottom up dp solution

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)) == 1:
            return nums[0]

        dp = [0 for h in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])

        return dp[len(nums)-1]
```

<br>

#### Explanation

Use tabulation using DP array.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of houses or the size of the input array.

- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the size of the dp array.

<br>
<br>

### Bottom up dp solution with space optimisation

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev_to_prev = nums[0]
        prev = max(nums[0], nums[1])

        for house in range(2,len(nums)):
            robbed = max(prev, nums[house]+prev_to_prev)
            prev_to_prev = prev
            prev = robbed

        return prev
```

<br>

#### Explanation

Use tabulation using two variables.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of houses or the size of the input array.

- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

Elegant (less code) version of the above algorithm, however less intuitive.

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

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

<br>
<br>
<br>

## Resources

- Neetcode's video is a good resource.

<br>
<br>
<br>
