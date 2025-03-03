# 153. Find Minimum in Rotated Sorted Array

Medium [level question on leetcode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/).

<br>
<br>
<br>

## Clarifications

- Are the elements unique?

  - It is mentioned that the elements are unique.

- Do we have to return the minimum value or the index of the minimum value?

  - Return the value.

- Is it always rotated?

  - Not necessarily.

<br>
<br>
<br>

## Test cases

| Case                                                                | Input       | Output |
| ------------------------------------------------------------------- | ----------- | ------ |
| Single element                                                      | [7]         | 7      |
| Un-rotated array containing two elements (adds as even case aswell) | [1,2]       | 1      |
| Rotated array containing two elements                               | [2,1]       | 1      |
| Un-rotated array containing more elements (adds as odd case aswell) | [1,2,3,4,5] | 1      |
| Rotated array containing more elements                              | [4,5,1,2,3] | 1      |

Broadly the tests can be divided into inputs containing :

- Rotated arrays and non-rotated arrays.
- Arrays with even elements and odd elements.

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
    def findMin(self, nums: List[int]) -> int:
        pivot_value = float('inf')
        low = 0
        high = len(nums)-1

        while(low <= high):
            mid = (high+low)//2
            if (nums[low] <= nums[mid]):
                pivot_value = min(pivot_value, nums[low]) # left half of mid, including mid is sorted.
                low = mid + 1 # low's value is the min in that part, store that and get rid of the part
            else:
                pivot_value = min(pivot_value, nums[mid]) # right half of mid, including mid is sorted.
                high = mid - 1  # mid's value is the min in that part, store that and get rid of the part
        return pivot_value
```

```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int pivot_value = INT_MAX;
        size_t low = 0;
        size_t high = nums.size()-1;

        while(low <= high){
            size_t mid = low + ((high-low)/2);

            if(nums.at(low) <= nums.at(mid)){
                pivot_value = std::min(pivot_value, nums.at(low));
                low = mid + 1;
            }
            else{
                pivot_value = std::min(pivot_value, nums.at(mid));
                high = mid - 1;
            }
        }
        return pivot_value;
    }
};
```

<br>

#### Explanation

Identify the sorted half by comparing low and mid's value. Record the minimum in the sorted half and update the pointers to eliminate that half.

- Compare the values at low and mid to identify the sorted half. If low is less than mid, the left half is sorted, and low is the minimum; we store it and eliminate the left half by updating the low pointer. Conversely, if low is greater than mid, the right half is sorted, and mid is the minimum; we store it and eliminate the right half by updating the high pointer. This process iteratively narrows the search until the minimum is found.

- `while(low <= high)`, the equality is needed for cases like `[5]`.

- `if(nums.at(low) <= nums.at(mid))`, the equality is needed for cases like `[2,1]`.

<br>

#### Complexity analysis

- Time Complexity : This is a logarithmic, $O(log(n))$ solution in terms of time, where $n$ is the size of the input array.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>

#### Elegant implementation

```py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        while(low < high):
            mid = (high+low)//2
            if (nums[mid] >= nums[high]):
                # array is definitely rotated and pivot has to be towards right of mid. ex: [3,4,5,1,2]
                low = mid + 1
            else:
                # array could be rotated ex: [6,2,3,4,5] or unrotated ex: [1,2,3].
                # either way, pivot will be at mid or left of mid
                high = mid
        return nums[low]
```

Use modified binary search. Compare mid's value with high's value instead of comparing it with lows value.

- If mid's value is greater than high's value, then it means that the array is definitely rotated and the pivot has to be towards the right of mid. Otherwise the pivot could be at mid or left of it.

- Comparing mid's value with low's value is much more [complicated](#complex-implementation)!

- Not intuitive.

<br>

#### Complex implementation

```py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[low]:
                # array could be rotated or un-rotated.
                if nums[high] < nums[low]:
                    #array definitely rotated. ex: [3,4,5,1,2] and pivot is towards right of mid
                    low = mid + 1
                else:
                    #array definitely not rotated. ex: [1,2,3,4,5] and pivot has to be first element
                    return nums[low]
            elif nums[mid] < nums[low]:
                # array definitely rotated. ex: [5,1,2,3,4] and pivot can be at mid or towards its left
                high = mid
            else:
                # nums[mid] == nums[low]
                if nums[mid] < nums[high]:
                    #ex: [1,2]
                    return nums[low]
                else:
                    #ex: [2,1]
                    low += 1

        return nums[low]
```

If we develop an algorithm using comprision between mid value and low value, we need to cover a lot of cases. Precisely because in the case where array could be rotated or un-rotated, the pivot can lie towards either side of mid and also there is an extra edge case.

- Not intuitive and complex.

<br>
<br>
<br>

## Follow ups

- Implement algorithm to return the index instead of the value.

```py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = float('inf')
        pivot_value = float('inf')
        low = 0
        high = len(nums)-1

        while(low <= high):
            mid = (high+low)//2
            if (nums[low] <= nums[mid]):
                pivot_value = min(pivot_value, nums[low])
                if(pivot_value == nums[low]):
                    pivot = low #update pivot only if the pivot_value is updated
                low = mid + 1
            else:
                pivot_value = min(pivot_value, nums[mid])
                if(pivot_value == nums[mid]):
                    pivot = mid
                high = mid - 1
        return pivot
```

- Implement algorithm to return the number of times the array is rotated to get that configuration.

  - The zero based index of the pivot value is equvivalent to the number of times the array is rotated! Hence the above algorithm will be the answer.

<br>
<br>
<br>

## Notes

<br>
<br>
<br>

## Resources

- The main [solution](#logarithmic-solution) is picked up from [Striver's video](https://www.youtube.com/watch?v=nhEMDKMB44g)

<br>
<br>
<br>
