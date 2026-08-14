# 128. Longest Consecutive Sequence

Medium [level question on leetcode](https://leetcode.com/problems/longest-consecutive-sequence/description/).

<br>
<br>
<br>

## Clarifications

1. Is the array sorted?
   - The array is unsorted.

1. Is the array comprised of unique elements?
   - No, duplicates are possible.

1. What is the type of data stored in the array?
   - Integers, hence positive, negative and zeros are possible.

1. Can the array be modified?
   - No such criteria

1. Can the array be empty?
   - Yes, `0 <= nums.length <= 105`

<br>
<br>
<br>

## Test cases

| Case                                         | Input                 | Output |
| -------------------------------------------- | --------------------- | ------ |
| Empty Array                                  | []                    | 0      |
| Array with single element                    | [100]                 | 1      |
| Array with no consecutive sequence           | [1,10,100]            | 1      |
| Array with dupliates                         | [1,2,2,3,8]           | 3      |
| Array with polarity                          | [-1,0,1]              | 3      |
| Array with longer consecutive sequence first | [1,2,3,8,10,11]       | 3      |
| Array with longer consecutive sequence later | [1,2,3,5,10,11,12,13] | 4      |
| Array with unsorted integers                 | [3,1,2,5]             | 3      |

<br>
<br>
<br>

## Solution

<br>
<br>

### Linear solution

```py
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        res = 0
        for num in uniqueNums:
            if num-1 not in uniqueNums:
                curNum = num
                curLen = 1
                while curNum+curLen in uniqueNums:
                    curLen += 1
                res = max(res, curLen)
        return res
```

```cpp
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> unique_nums;
        for(const auto& num:nums){      //O(n)
            unique_nums.insert(num);    //O(1) in the case of unordered_set and O(logn) in the case of set.
        }

        int res{0};
        int cur_length{0};
        for(auto num:unique_nums){  //O(m)
            cur_length = 1;
            auto is_found = unique_nums.find(num-1);    //O(1)
            if(is_found != unique_nums.end()){
                continue;
            }
            else{
                auto next_num = unique_nums.find(++num);
                while(next_num != unique_nums.end()){
                    ++cur_length;
                    next_num = unique_nums.find(++num);
                }
            }
            res = std::max(res, cur_length);
        }
        return res;
    }
};
```

<br>

#### Explanation

Filter for unique starting elements and count their successive neighbors in the set.

- Remove duplicates by converting the array into a set.
- Identify the "start" of a consecutive sequence in the set
  - An element is only worthy of being a starting point if it is the absolute beginning of a sequence (i.e., element - 1 does not exist in the set).
- Count the consecutive sequence, If an element is a starting point, keep checking for the next consecutive integers (element + 1, element + 2, etc.) and track the length.
- Update the Maximum: Compare the length of this sequence to your current maximum and keep the larger value.
- Return the Result: Once the loop finishes, return the length of the longest sequence found.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of elements in the input array.
  - It takes $O(n)$ to convert the input array into a set.
  - While iteration, every element is visited only once therefore $O(n)$ operation, even though it might look quadratic because of nested loop.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is number of elements in the input array. .
  - In the worst case, if the entire input array forms a consecutive sequence then the set will have to store all "n" elements.

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
