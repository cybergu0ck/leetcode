# 435. Non-overlapping Intervals

Medium [level question on leetcode](https://leetcode.com/problems/non-overlapping-intervals/description/).

<br>
<br>
<br>

## Clarifications

1. Is the array sorted?
   - No

1. Is the array comprised of unique elements?
   - No

1. What is the type of data stored in the array?
   - list containing two integers.

1. Can the array be modified?
   - No criteria

1. Can the array be empty?
   - No, `1 <= intervals.length <= 105`

1. Are the interval boundaries to be considered inclusive for overlapping criteria?
   - Intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

<br>
<br>
<br>

## Test cases

| Case                             | Input                        | Output |
| -------------------------------- | ---------------------------- | ------ |
| No overlapping                   | [[1,2], [5,6]]               | 0      |
| Duplicates                       | [[1,5],[1,5]]                | 1      |
| Partial overlapping              | [[1,5],[3,10],[4,15]]        | 2      |
| Complete overlapping             | [[1,50],[1,5]]               | 1      |
| Parital and complete overlapping | [[1,50],[1,5],[2,10],[4,15]] | 2      |

<br>
<br>
<br>

## Solution

<br>
<br>

### Quadratic solution

```py
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        toRemove = 0

        #count all the duplicates;
        uniqueIntervals = set()
        for interval in intervals:
            if tuple(interval) not in uniqueIntervals:
                uniqueIntervals.add(tuple(interval))
            else:
                toRemove +=1

        #sort the intervals based on the start index;
        sortedIntervals = sorted(uniqueIntervals, key = lambda pair:pair[0])

        #iterate over the sorted intervals;
        removedIntervals = set()
        for i in range(len(sortedIntervals)):
            for j in range(i+1, len(sortedIntervals)):
                firstInterval = sortedIntervals[i]
                secondInterval = sortedIntervals[j]
                if firstInterval not in removedIntervals and secondInterval not in removedIntervals:
                    if firstInterval[1] > secondInterval[0]:
                        #overlap
                        if firstInterval[1] < secondInterval[1]:
                            #keep first, remove second
                            removedIntervals.add(secondInterval)
                        else:
                            removedIntervals.add(firstInterval)
                            break

        toRemove += len(removedIntervals)
        return toRemove
```

```cpp

```

<br>

#### Explanation

Brute force approach with nested loop to remove overlapping intervals by comparing every pair.

- This is not the best approach in retrospect because of itense implementation!
- Handle the case for duplicates.
- Sort the unique intervals.
- Nested comparision and check every pair.
  - If there's an overlap, greedily choose to remove the interval that finishes later.

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(n^2)$ solution in terms of time, where $n$ is the number of intervals.
  - Checking for duplicates is $O(n)$.
  - The sorting operation is $O(n*log(n))$.
  - The nested loop is $O(n^2)$.
  - Overall, the quadratic component dominates.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the number of intervals.
  - The sets can take "n" space in the worst case.
  - Python's `sort` in the worst case can require $O(n)$ space for time sort.

<br>
<br>

### Logarithmic solution

```py
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        toRemove = 0
        intervals.sort()
        prevEnd = intervals[0][1]

        for interval in intervals[1:]:
            curStart = interval[0]
            curEnd = interval[1]
            if curStart < prevEnd:
                #overlap
                toRemove += 1
                prevEnd = min(prevEnd, curEnd)
            else:
                prevEnd = curEnd
        return toRemove
```

```cpp

```

<br>

#### Explanation

Use greedy approach. While iterating over the sorted intervals, keep the interval that ends earliest.

- It is greedy because at every step where there is a conflict, a choice has to be made that on what is best at the moment. In this specific case, when there is an overalp, greedily choose to remove the interval that finishes later, as it is more likely to cause future conflicts.
- Sort the intervals.
- Store the first interval's end value in `prevEnd` variable.
- Iterate over the other intervals. Every iteration there is a choice to be made,
  - If there's an overlap, the one with the earliest end value must be retained by updating `prevEnd`.
  - If there's no overlap, update the `prevEnd` with the current end value.

<br>

#### Complexity analysis

- Time Complexity : This is a logarithmic, $O(n*log(n))$ solution in terms of time, where $n$ is is the number of intervals.
  - The sorting operation is $O(n*log(n))$.
  - The loop iteration is $O(n)$.
  - Overall, the logarithmic component dominates.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.
  - Note that in this specific python code, the space complexity is linear, $O(n)$ as Python's `sort` in the worst case can require $O(n)$ space for time sort.

<br>
<br>
<br>

## Follow ups

- A minor optimization is to sort the intervals based on the "end time", This will avoid using `min` comparision. //REVIEW - Check if this is accurate

<br>
<br>
<br>

## Notes

- "greedy" approach is about making the best choice for the moment.

<br>

Python :

- Python's `sort` method uses CPython's timesort algorithm which has the following complexities, considering worst case scenarios.
  - $O(n*logn)$ for time.
  - $O(n)$ for space.
- For multidimensional lists, Python list's `sort` method automcatically sorts the inner lists based on the subsequent indices.
  - For 2d list, it sorts the inner lists based on the first index and relies on second index if the first indicies are equal.

<br>
<br>
<br>

## Resources

- [Solution](#logarithmic-solution) is from neetcode.

<br>
<br>
<br>
