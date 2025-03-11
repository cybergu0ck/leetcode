# 162. Find Peak Element

Medium [level question on leetcode](https://leetcode.com/problems/find-peak-element/description/).

<br>
<br>
<br>

## Clarifications

- Does it mean that no two consecutive elements have identical values.

  - Yes, it is mentioned that nums[i] != nums[i+1] for all valid i's.

- Can the input array be empty?

  - No, minimum of 1 element is present.

<br>
<br>
<br>

## Test cases

| Case                     | Input       | Output |
| ------------------------ | ----------- | ------ |
| single element           | [1]         | 0      |
| monotonically increasing | [1,2,3]     | 2      |
| monotonically decreasing | [3,2,1]     | 0      |
| valley                   | [3,1,3]     | 0 or 2 |
| hill                     | [1,3,1]     | 1      |
| hill valley hill         | [1,3,1,2,1] | 1 or 3 |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py

```

```cpp

```

<br>

#### Explanation

Perform linear search and comparer the neighbours to determine peak.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is size of the input array.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

### Efficient solution

```py
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while(l <= r):
            m = l + ((r-l)//2)
            if(m > 0 and nums[m] < nums[m-1]):
                r = m - 1
            elif(m < len(nums) - 1 and nums[m] < nums[m+1]):
                l = m + 1
            else:
                return m
```

```cpp

```

<!-- TODO - write the C++ code -->

<br>

#### Explanation

The question is set up such that we can use the concept of binary search without the condition of sortedness. Given an index, it is guaranteed that there will be a peak whicher ever side has higher values.

- Given an index, it is guaranteed that there will be a peak whicher ever side has higher values because on the increasing side, there could be a dip (dip itself will be a peak) or no dip (the last index will be the peak), either way a peak is guaranteed.

<br>

- If mid's value is lesser than it's left neighbor, it means that there ought to be a peak on the left. Update right pointer.
- After checking the above, if mids value is lesser than it's right neighbor, it means that there ought to be a peak on the right. Uspdate left poiter.
- If above two conditions are not met, it means that mid itself is peak.
- Add checks accordingly so that the array indexing doesnt fail (do it after intuitively coming up with the conditional)

<br>

#### Complexity analysis

- Time Complexity : This is a logarithmic, $O(log(n))$ solution in terms of time, where $n$ is size of the input array.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Coding the solution might seem difficult untill the crux of the logic is understood. Otherwise will end up in writing lot of complicated if else conditionals.

<br>
<br>
<br>

## Resources

- Solution is picked from [neetcode](https://www.youtube.com/watch?v=kMzJy9es7Hc)

<br>
<br>
<br>
