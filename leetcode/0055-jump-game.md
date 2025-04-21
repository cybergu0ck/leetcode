# 55. Jump Game

Medium [level question on leetcode](https://leetcode.com/problems/jump-game/description/).

<br>
<br>
<br>

## Clarifications

- Can the elements of the input array be negative or zero?
  - It can be zero but not negative. The given constraint is `0 <= nums[i] <= 105`.

<br>
<br>
<br>

## Test cases

| Case                                        | Input       | Output |
| ------------------------------------------- | ----------- | ------ |
| Single element                              | [0]         | True   |
| Non-zero elements                           | [2,3,1,1,4] | True   |
| Zero in between (uncrossable valley)        | [3,2,1,0,4] | False  |
| Zero in between (crossable valley)          | [3,3,1,0,4] | True   |
| Zero at the start                           | [0,3,1]     | False  |
| Step to goal exits but step to step doesn't | [1,0,1,0]   | False  |

<br>
<br>
<br>

## Solution

<br>
<br>

### Recursive solution

```py
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def rec(i):
            if(i == 0):
                return True

            for j,v in enumerate(nums[:i]):
                if(j + v >= i and rec(j)):
                    return True
            return False

        return rec(len(nums)-1)
```

```cpp

```

<br>

#### Explanation

Use the framework for solving recusrive question

- The question doesn't appear to be a DP question as it asks whether it is possible to reach the last index. The last index can be reached if at least one way is feasible. Therefore, phrasing the question as number of ways to reach the last index turns it into a DP question since it is somewhat combinatorial.

- The problem has overlapping subproblems: Given an index, we check if it can be reached from any of the previous indices.

1.  Define the objective function.

    $T(i)$ is wether the index $i$ can be reached starting at index 0.

2.  Identify the base cases.

    $T(0) = True$

    - The last index and first index is same and therefore already at the last index.

3.  Form the recurrance relation.

    $T(i) = \bigvee_{j=0}^{i-1} \left( T(j) \land (j + nums[j] \geq i) \right) \quad \text{if } i > 0$

    - This is a recursive leap of faith, meaning we are assuming we know the answers to the previous problems.
    - Given a target index, check if the target index can be reached from any of the previous indices. Early return if it is possible.

4.  Find the answer.

    The final value returned is the answer to the whole problem.

<br>

#### Complexity analysis

- Time Complexity : This is a exponential, $O(n^n)$ solution in terms of time, where $n$ is size of the input array.

  - An illustration of the recursive tree,

    <!-- TODO add the image -->

  - The time complexity is determined by the number of recursive calls which is equal to the number of nodes in the recursive tree. In the worst case, the depth of the recursive tree and the branching per node will be equal to $n$ when the last index can be reached from every previous index.The maximum number of nodes for a tree with depth n and each node having n branches is $n^n$. Checkout [trees](https://github.com/cybergu0ck/notes/blob/main/engineering/software/fundamentals/data-structures/trees/01-trees.md).

  <!-- TODO check if the above generalised version of the equation is present in the notes  -->

- Space Complexity : This is a linear, $O(n)$ solution in terms of space. This is the auxilary stack space.
  - Technically, it is the depth of the recursive tree.

<br>
<br>

### Top down dp solution

```py
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def rec(i):
            if(i in memo):
                return memo[i]
            if(i == 0):
                return True

            for j,v in enumerate(nums[:i]):
                if(j + v >= i and rec(j)):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return rec(len(nums)-1)
```

```cpp

```

<br>

#### Explanation

Memoize the recursive solution using a map.

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(n^2)$ solution in terms of time, where $n$ is the size of the input array.

  - Memoization ensures that each state (i.e., each index i) is computed at most once. However, for each index i, the function loops over all previous indices.

    <!-- REVIEW Is it O(n) or O(n2) -->

- Space Complexity : This is a linear, $O(n)$ solution in terms of space. Where $n$ is the size of the map.

<br>
<br>

### Bottom up dp solution

```py
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for i in nums]
        dp[0] = True

        for i,v in enumerate(nums[1:], start=1):
            for j in range(i):
                if(j + nums[j] >= i and dp[j]):
                    dp[i] = True
                    break

        return dp[-1]
```

```cpp

```

<br>

#### Explanation

Tabulation using 1D array.

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(n^2)$ solution in terms of time, where $n$ is the size of the input array.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space. Where $n$ is the size of the 1D dp array.

<br>
<br>

### Greedy solution

```py
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if(i + nums[i] >= target):
                target = i

        return True if target == 0 else False
```

```cpp

```

<br>

#### Explanation

Use a backward greedy approach that updates the target position to the earliest index from which the end is reachable, ultimately checking if the start index can reach the end.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the size of the input array.

- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>

#### Implementation

Greedy approach with forward iteration, track the farthest reachable index at each step of forward iteration and return false if the current index exceeds this reach.

```py
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0

        for i in range(len(nums)):
            if(i > reachable):
                return False
            else:
                reachable = max(reachable, i + nums[i])

        return True
```

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- The recursive solution and the bottom up dp solution times out on leetcode because of large input however the top down dp solution passes. I am assuming because of the nature of the implementation, slight tweak in the implementation will lead of time out.

- Checkout both implementations of the greedy solution. One with forward iteration and another with backward.

<br>
<br>
<br>

## Resources

- The greedy solution with backward iteration is copied from [neetcode](https://www.youtube.com/watch?v=Yan0cv2cLy8).
- The greedy solution with forward iteration is copied form [Techdose](https://www.youtube.com/watch?app=desktop&v=muDPTDrpS28&t=618s).

<br>
<br>
<br>
