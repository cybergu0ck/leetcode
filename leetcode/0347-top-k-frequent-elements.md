# Template

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/top-k-frequent-elements/description/).

- Some good follow ups are:

<br>
<br>

## Test Cases

<br>
<br>

## Solution

<br>

### Brute Force

```cpp
#include <unordered_map>
#include <vector>
#include <utility>
#include <algorithm>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> num_to_count;
        for(const auto& num : nums){    //O(n)
            ++num_to_count[num];
        }

        std::vector<std::pair<int,int>> temp_vec;
        for(const auto& pair : num_to_count){
            temp_vec.push_back(pair);
        }

        std::sort(temp_vec.begin(), temp_vec.end(), [](std::pair<int,int> a, auto b){return a.second > b.second;});   //mO(m)

        std::vector<int> res;
        for(int i=0; i < k; ++i){
            res.push_back(temp_vec[i].first);
        }

        return res;
    }
};
```

```py

```

- This is a $O(n * log(n))$ solution in terms of time, where $n$ is the number of unique elements in the input vector.
- This is a $O(n)$ solution in terms of space, where $n$ is the number of unique elements in the input vector.

<br>

### Efficient Solution

```py

```

- This is a $O()$ solution in terms of time and $O()$ solution in terms of space.

<br>

### Ideal Solution

```py

```

- This is a $O()$ solution in terms of time and $O()$ solution in terms of space.

<br>
<br>

## Notes

<br>
<br>

## Resources

<br>
<br>
