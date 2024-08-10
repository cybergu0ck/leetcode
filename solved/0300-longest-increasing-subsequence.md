# 300. Longest Increasing Subsequence

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/longest-increasing-subsequence/description/).

- Some good follow ups are:

  1. Are we supposed to consider strictly increasing subsequence? or

- Checkout the notes section first!

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

Solving the question using Dynamic Programming as the question it poses is similar to "what is the longest ...", which is type of optimization DP question.

- Using the DP frameork,

  1. The Objective Function, $F(i)$ is longest increasing sequence ending at index i.
     1. This does not necessarily represent the longest subsequence that includes all elements up to the i'th index.
     2. Instead, it specifically looks at subsequences that have nums[i] as their last element.
  2. The Base Case, $F(0) = 1$. The longest increasing sequence at zeroth index is 1.
  3. The Recurrance Relation, $F(n) = 1+F(j)$ if $nums[j]<nums[n]$ otherwise 1 , for j from 0 to n.
  4. The Answer, The answer is not present in F(n) like usual. The answer is $max(F(n))$ for n from 0 to n.

<br>

#### Recursive Solution (Top Down Approach)

```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def lengthOfLISEndingAtIndex(endIndex):
            if endIndex == 0:
                return 1
            longest = 1
            for i in range(endIndex):
                if nums[i] < nums[endIndex]:
                    length = 1 + lengthOfLISEndingAtIndex(i)
                    longest = max(longest, length)

            return longest

        res = 1
        for i in range(len(nums)):
            curRes = lengthOfLISEndingAtIndex(i)
            res = max(res, curRes)

        return res
```

- Since a subsequence of a increasing sequence must also be increasing sequence, we can try DP. In this case it is a optimization type of DP.
- If this were a classic top down appraoch we should have called the recursive function with the last index but it is not the case here. Because of the nature of the question, There is a sense of direction (from left to right). Hence we have to iterate over every case until the given index and pick the maximum one.
- The following has $O(2^n)$ time complexity $O(n)$ space complexity.

<br>

#### Recursive Solution (Top Down Approach) with Memoization

```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def lengthOfLISEndingAtIndex(endIndex):
            if endIndex in memo:
                return memo[endIndex]
            if endIndex == 0:
                return 1
            longest = 1
            for i in range(endIndex):
                if nums[i] < nums[endIndex]:
                    length = 1 + lengthOfLISEndingAtIndex(i)
                    longest = max(longest, length)
            memo[endIndex] = longest
            return longest

        res = 1
        for i in range(len(nums)):
            curRes = lengthOfLISEndingAtIndex(i)
            res = max(res, curRes)

        return res
```

- The following has $O(n^2)$ time complexity $O(n)$ space complexity.
  - The time complexity of the recursive calls is cut down to $O(n)$ because of memoization. The outer loop has $O(n)$ hence overall time complexity is $O(n^2)$.
  - The space used by the dictionary is $O(n)$ and the auxilary space is also $O(n)$. Overall, It is $O(n)$.

<br>

#### Dynamic Programming Solution (Bottom Up Approach)

```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for num in nums]

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)
```

- The following has $O(n^2)$ time complexity $O(n)$ space complexity.
  - The space complexity of this this cannot be reduced further by using variables instead of the array because the answer is not always in the previous state.

<br>

### Ideal Solution

```py

```

- The following has $O()$ time complexity $O()$ space complexity.

<br>
<br>

## Notes

<br>

### Subsequence

_A subsequence of a sequence is a new sequence derived from the original sequence by deleting some or no elements without changing the order of the remaining elements._

- For a sequence [3, 6, 7, 1, 5],
  - [3,7,1] is a subsequence.
  - [7] is a subsequence.
  - [7,6,5] is not a subsequence because the original index of 6 is less than that of 7.

<br>

### Strictly Increasing Sequence

_A sequence is strictly increasing if every element is greater than the previous one._

- [1, 3, 5, 7] is a strictly increasing sequence.
- [1, 3, 5, 5] is not a strictly increasing sequence.

<br>

### Non decreasing Sequence

_A sequence is non-decreasing if every element is greater than or equal to the previous one._

- [1, 3, 5, 5] is a non decreasing sequence.

<br>
<br>

## Test Cases

<br>
<br>

## Resources

<br>
<br>
