# 33. Search in Rotated Sorted Array

Medium [level question on leetcode](https://leetcode.com/problems/search-in-rotated-sorted-array/description/).

<br>
<br>
<br>

## Clarifications

- It is mentioned that the elements are distinct.
- It is mentioned to return -1 if the element to be searched is not present.

<br>
<br>
<br>

## Test cases

| Case                | Input                          | Output |
| ------------------- | ------------------------------ | ------ |
| Target presesnt     | [4,5,6,7,0,1,2] and target = 0 | 4      |
| Target not presesnt | [4,5,6,7,0,1,2] and target = 3 | -1     |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

<br>

#### Explanation

Perform linear search by iterating over the entire array.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is size of the input array.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

### Logarithmic solution

```py
class Solution:
    def find_pivot_index(self, nums: List[int]) -> int:
        pivot_value = float('inf')
        low = 0
        high = len(nums)-1

        while(low <= high):
            mid = (high+low)//2
            if (nums[low] <= nums[mid]):
                pivot_value = min(pivot_value, nums[low])
                low = mid + 1
            else:
                pivot_value = min(pivot_value, nums[mid])
                high = mid - 1
        return pivot_value

    def search(self, nums: List[int], target: int) -> int:
        res = -1
        low = 0
        high = len(nums)-1
        pivot = self.find_pivot_index(nums)

        if (nums[pivot] == target):
            res = pivot
        else:
            if (target >= nums[pivot] and target <= nums[high]):
                low = pivot
            else:
                high = pivot - 1

            #binary search
            while(low <= high):
                mid = (low + high)//2
                if(target == nums[mid]):
                    res = mid
                    break
                elif(target < nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1

        return res

```

```cpp

```

<!-- TODO - complete the cpp implementationhttps://leetcode.com/problems/search-in-rotated-sorted-array/description/ -->

<br>

#### Explanation

After obtaining the pivot, divide the array into two sorted halves. Determine which half contains the target, then conduct a binary search in that half.

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

- Know how to find the pivot. Checkout [Find Minimum in Rotated Sorted Array](./0153-find-minimum-in-rotated-sorted-array.md)

<br>
<br>
<br>

## Resources

- Checkout [Find Minimum in Rotated Sorted Array](./0153-find-minimum-in-rotated-sorted-array.md)

<br>
<br>
<br>
