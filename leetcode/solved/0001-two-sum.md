# Two Sum

Easy level [question on leetcode](https://leetcode.com/problems/two-sum/description/).

<br>
<br>
<br>

## Clarifications

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute Force

```py
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            for j, w in enumerate(nums):
                if i != j:
                    if v + w == target:
                        return [i, j]

```

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        std:vector<int> res;
        for(int i = 0; i < nums.size(); i++)
        {
            for(int j= i+1; j < nums.size(); j++)
            {
                if(nums[i] + nums[j] == target)
                {
                    res.push_back(i);
                    res.push_back(j);
                    break;
                }
            }
        }
        return res;
    }
};
```

<br>

#### Explanation

Determine the indices by iterating over every possible combination.

<!-- detailed explanation with steps if appropriate -->

<br>

#### Complexity Analysis

- **Time Complexity**: This is a quadratic $O(n^2)$ solution in terms of time, where $n$ is the size of the input array.
- **Space Complexity**: This is a constant $O(1)$ solution in terms of space.

<br>
<br>

### Efficient Solution

```py
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, value in enumerate(nums):
            needed = target - value
            if needed in map:
                return [index, map[needed]]
            map[value] = index
```

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        std::unordered_map<int, int> track;
        std:vector<int> res;
        for(int index=0; index < nums.size(); index++)
        {
            int needed = target - nums[index];
            if(track.find(needed) != track.end())
            {
                res.push_back(index);
                res.push_back(track[needed]);
                break;
            }
            else
            {
                track[nums[index]] = index;
            }
        }
        return res;
    }
};
```

<br>

#### Explanation

Iterate over the array and utilize a dictionary which stores the complement of each element needed to reach the target sum.

<!-- detailed explanation with steps if appropriate -->

<br>

#### Complexity Analysis

- **Time Complexity**: This is a linear $O(n)$ solution in terms of time, where $n$ is the size of the input array.
- **Space Complexity**: This is a linear $O(n)$ solution in terms of space, where $n$ is the size of the input array.

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
