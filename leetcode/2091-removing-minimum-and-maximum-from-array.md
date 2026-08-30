# 2091. Removing Minimum and Maximum From Array

Medium [level question on leetcode](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/description/).

At its core, this problem is about minimizing the deletion cost to clear two target indices from an array. Deletion is restricted only from two points, left most and right most side.

<br>
<br>
<br>

## Clarifications

1. What is the type of data stored in the array?
   - Integers

1. Is the array sorted?
   - No

1. Is the array comprised of unique elements?
   - Yes

1. Can the array be modified?
   - No constraint mentioned, so yes.

1. Can the array be empty?
   - No, 1 <= nums.length <= 105

<br>
<br>
<br>

## Test cases

| Case                                        | constraint type | Input          | Output |
| ------------------------------------------- | --------------- | -------------- | ------ |
| Targets are same item                       | size            | [1]            | 1      |
| Targests are adjacent items                 | size/position   | [1,2]          | 2      |
| Targets are on one same end (left or right) | position        | [-10,10,5,6,7] | 2      |
| Targets are on opposite end                 | position        | [-10,5,6,7,10] | 2      |
| Targets are closely in middle               | position        | [5,-10,10,6]   | 3      |
| One target is present at the end            | position        | [5,-10,6,7,10] | 3      |

- Must not focus on min and max, it doesn't matter. Consider them as targets to be removed!
- Most of the test cases are testing positional constraints and couple of size constraints.

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        if(len(nums) == 1):
            return 1
        #create a map of value and index
        ValueToIndex = {}
        for i,v in enumerate(nums):
            ValueToIndex[v] = i

        startIndex = 0
        endIndex = len(nums)-1
        minValue = min(nums)
        maxValue = max(nums)
        minValueIndex = ValueToIndex[minValue]
        maxValueIndex = ValueToIndex[maxValue]

        #pick the one that is closer to an end
        leftOfMinValue = abs(minValueIndex - 0)
        rightOfMinValue = abs(minValueIndex - endIndex)

        leftOfMaxValue = abs(maxValueIndex - 0)
        rightOfMaxValue = abs(maxValueIndex - endIndex)

        firstToDeleteIndex = -1
        secondToDeleteIndex = -1

        closest = min(leftOfMinValue, rightOfMinValue, leftOfMaxValue, rightOfMaxValue)
        if(closest == leftOfMinValue or closest == rightOfMinValue):
            firstToDeleteIndex = minValueIndex
            secondToDeleteIndex = maxValueIndex
        elif(closest == leftOfMaxValue or closest == rightOfMaxValue):
            firstToDeleteIndex = maxValueIndex
            secondToDeleteIndex = minValueIndex

        #first pick the one on the left
        onLeft = abs(firstToDeleteIndex - 0)
        onRight = abs(firstToDeleteIndex - endIndex)
        firstBest = min(onLeft, onRight)
        if(firstBest == onLeft):
            startIndex = firstBest + 1
        else:
            endIndex = endIndex - firstBest - 1

        #now pick the right one
        onLeft = abs(secondToDeleteIndex - startIndex)
        onRight = abs(secondToDeleteIndex - endIndex)
        bestForRight = min(onLeft, onRight) + 1

        return firstBest + bestForRight + 1
```

```cpp

```

<br>

#### Explanation

Greedy solution, remove the targest closest to an end and then remove the other.

- This is NOT the best approach, too much combersome and lot of edge cases.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of elements in the input array.
  - Creating ValueToIndex via enumerate takes $\mathcal{O}(N)$ time.
  - min(nums) and max(nums) each take $\mathcal{O}(N)$ time.
  - All remaining conditional checks and arithmetic operations are $\mathcal{O}(1)$.
  - Total time is $N + N + N = 3N \Rightarrow \mathcal{O}(N)$.
- Space Complexity : This is a lienar, $O(n)$ solution in terms of space, where $n$ is number of elements in the input array.
  - The ValueToIndex hash map stores $N$ key-value pairs, requiring $\mathcal{O}(N)$ auxiliary space.

<br>
<br>

### Cleaner solution

```py
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        endIndex = len(nums)-1
        i = nums.index(min(nums))
        j = nums.index(max(nums))

        lowIndex = min(i,j)
        highIndex = max(i,j)

        deleteFromLeft = highIndex + 1
        deleteFromRight = endIndex - lowIndex + 1
        deleteFromBothEnds = lowIndex + 1 + endIndex - highIndex + 1
        return min(deleteFromLeft, deleteFromRight, deleteFromBothEnds)
```

```cpp

```

<br>

#### Explanation

The optimal strategy is always the minimum of three static options: delete both from the left, delete both from the right, or delete one from each end.

- Find Positions: Identify the 0-based indices of the minimum and maximum elements, defining $low = \min(i, j)$ and $high = \max(i, j)$
- Option 1 (Both Left): Clear from start up to $high \rightarrow$ Cost $= high + 1$.
- Option 2 (Both Right): Clear from end down to $low \rightarrow$ Cost $= endIndex - low + 1$.
- Option 3 (Split Both Ends): Clear $low$ from start and $high$ from end $\rightarrow$ Cost $= (low + 1) + (endIndex - high + 1)$.
- Final Answer: Return $\min(\text{Option 1}, \text{Option 2}, \text{Option 3})$.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of elements in the input array.
  - min(nums) and max(nums) each scan the array once in $\mathcal{O}(N)$ time.
  - nums.index(...) performs an $\mathcal{O}(N)$ linear scan to retrieve the indices.
  - All index sorting and option comparisons take $\mathcal{O}(1)$ time.
  - Total Time: $\mathcal{O}(N)$

- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

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

<br>
<br>
<br>
