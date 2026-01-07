# 56. Merge Intervals

Medium [level question on leetcode](https://leetcode.com/problems/merge-intervals/description/).

<br>
<br>
<br>

## Clarifications

- Are the boundaries of intervals inclusive or exclusive while considering overlap?

  - Inclusive, [[1,2],[2,5]] should return [1,5].

- Can there be gaps between intervals?

  - Yes, intervals can be [[1,2],[5,6]]

- Is the starti <= endi for any interval i?

  - Yes, `0 <= starti <= endi <= 104`

- Are intervals arranged in order in intervals?

  - No, intervals can be [[4,10], [1,6]]

- Can the intervals array be empty?

  - No, `1 <= intervals.length <= 104`

- Is the interval item in intervals guaranteed to be of size 2?
  - Yes, `intervals[i].length == 2`

<br>
<br>
<br>

## Test cases

| Case             | Input         | Output        |
| ---------------- | ------------- | ------------- |
| Partial overlap  | [[1,5],[2,8]] | [1,8]         |
| Complete overlap | [[1,6],[2,3]] | [1,6]         |
| No overlap       | [[1,3],[4,8]] | [[1,3],[4,8]] |

- The above cases are sufficient after considering ascending order of intervals. i.e `interval[i][0] <= interval[i+1][0]`

  - Note that there will be more than the above three cases if orderness of interval array is not considered!

<br>
<br>
<br>

## Solution

<br>
<br>

### Logarithmic solution

```py
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals array based on the first index of each item
        intervals.sort(key = lambda x:x[0]) #n log(n)

        res = []
        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
            elif res[-1][1] >= interval[0] and res[-1][1] <= interval[1]:
                #Partial overlap
                res[-1] = [res[-1][0], interval[1]]
            elif res[-1][1] >= interval[0] and res[-1][1] >= interval[1]:
                #Full overlap
                res[-1] = [res[-1][0], res[-1][1]]
            else:
                res.append(interval)
        return res
```

```cpp

```

<br>

#### Explanation

Sort the intervals array and starting from first interval, check if subsequent intervals either partially or fully overlap or don't overlap.

- Sort the intervals array based on the start value of each interval.
- Check for the three cases and upate the result array.

<br>

#### Complexity analysis

- Time Complexity : This is a logarithmic, $O(n*log(n))$ solution in terms of time, where $n$ is number of items present in the input array.
  - sorting array takes $O(n*log(n))$ and iterating over the array is $O(n)$. Overall, it takes logarithmic.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is s size of the result array.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- I was not able to understand the question intially. Was able to understand it with the help of an example. Seek an example if the question seems complicated or vague!

- I was able to figure out the logic but was unable to code it up correctly. Practice and get exposed to different approaches!

- Sorting an array is logarithmic $O(n*log(n))$.

<br>

Python :

- `sort` is inplace and must be called on the list object and `sorted` returns a new list and a list must be passed to it.

  - Example : `nums.sort()` and `sorted(nums)`
  - Both have the same time complexity i.e. $O(n*log(n))$.

- Sorting nested lists using `key`.

  ```py
  array_2d = [[2,5], [1,3]]
  arry_2d.sort(key = lambda x:x[0]) #sorts the items based on the first value in the item
  print(array_2d)

  #[[1,3],[2,5]]
  ```

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
