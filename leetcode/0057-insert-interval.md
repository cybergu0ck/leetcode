# 57. Insert Interval

Medium [level question on leetcode](https://leetcode.com/problems/insert-interval/description/).

<br>
<br>
<br>

## Clarifications

1. What is the type of data stored in the array?
   - The array contains arrays comprised of two integers always.

1. Is the array sorted?
   - Yes, sorted based on the first index of the inner array.

1. Is the array comprised of unique elements?
   - Yes, it is mentioned that intervals are non-overlapping.

1. Can the array be modified?
   - Note that you don't need to modify intervals in-place. You can make a new array and return it.

1. Can the array be empty?
   - `0 <= intervals.length <= 104`

<br>
<br>
<br>

## Test cases

| Case                                 | Input                                                     | Output              |
| ------------------------------------ | --------------------------------------------------------- | ------------------- |
| Empty intervals                      | intervals = [], newInterval = [5,7]                       | [[5,7]]             |
| Insert before all intervals          | intervals = [[3,5],[6,9]], newInterval = [1,2]            | [[1,2],[3,5],[6,9]] |
| Insert after all intervals           | intervals = [[1,2],[3,5]], newInterval = [6,9]            | [[1,2],[3,5],[6,9]] |
| Insert in middle (no overlap)        | intervals = [[1,2],[6,9]], newInterval = [3,5]            | [[1,2],[3,5],[6,9]] |
| Exact duplicate of existing interval | intervals = [[1,3],[6,9]], newInterval = [1,3]            | [[1,3],[6,9]]       |
| Overlap multiple intervals           | intervals = [[1,3], [6,9], [12,15]], newInterval = [9,13] | [[1,3], [6,15]]     |

<br>

- Lot of unique cases will be taken care by considering a superior test case. Example : Merge with single interval cases and boundary touch cases are taken care in the "Overlap multiple intervals" case itself.

<br>
<br>
<br>

## Solution

<br>
<br>

### Linear solution

```py
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newStart, newEnd = newInterval

        for i, (start, end) in enumerate(intervals):
            if(newEnd < start):
                # new interval comes before the current interval
                res.append([newStart, newEnd])
                return res + intervals[i:]
            if(newStart > end):
                #new interval comes after the current interval
                res.append([start, end])
            else:
                #overlapping case
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)

        res.append([newStart, newEnd])
        return res
```

```cpp

```

<br>

#### Explanation

Iterate over the sorted array and insert the newInterval appropriately.

- This is the kind of question which has straight forward logic but is difficult to implement as one can miss the test cases.
- Essentially, there are only three conditionals:
  1. Insert the interval before the current interval, an early return case.
  1. Insert the interval later, append the current interval to result and move forward.
  1. Overlap present, modify the `newInterval` itself (`newStart` and `newEnd` in this case) so that the next iterations are taken care!
  - Note that the `newInterval` needs to be added after the loop, since the early return is not executed it means the `newInterval` has to be inserted after all the intervals.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is length of the input array.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space, without considering the result array.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- The original implementation having the same algorithm as [linear solution](#linear-solution) authored by me was as follows :

  ```py
  class Solution:
      def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
          res = []

          for i in range(len(intervals)):
              curInterval = intervals[i]
              curStart = curInterval[0]
              curEnd = curInterval[1]
              newStart = newInterval[0]
              newEnd = newInterval[1]

              if(newEnd < curStart):
                  res.append(newInterval)
                  res.extend(intervals[i:])
                  return res
              elif(newStart <= curEnd):
                  minValue = min(curStart, newStart)
                  maxValue = max(curEnd, newEnd)
                  newInterval = [minValue, maxValue]
              else:
                  res.append(curInterval)

          res.append(newInterval)
          return res
  ```

- The [linear solution](#linear-solution) is improved version because of the following:
  - Utilising `newStart` and `newEnd` instead of `newInterval`.
    - Unpacking it avoids the indexing.
  - Using enumeration along with unpacking to avoid indexing current interval values.
  - Ordering if conditionals better, "insert before", "insert later" if both fails then it means the "overlapping" case and we don't need to think for a condition.

<br>
<br>
<br>

## Resources

- I saw [neetcode]() solution video.

<br>
<br>
<br>
