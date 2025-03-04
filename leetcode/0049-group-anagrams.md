# Template

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/group-anagrams/description/).

- Some good follow ups are:
  1. About the characters of the string, are they all alphabets, alphanumeric or all out ascii.

<br>
<br>

## Test Cases

<br>
<br>

## Solution

<br>

### Brute Force

```py

```

- This is a $O()$ solution in terms of time and $O()$ solution in terms of space.

<br>

### Quasi-quadratic Solution

Sort each string in the input vector, use that as the key and store the actual string in a vector which will be the value of the map.

<br>

```py

```

//TODO - Write the python code

- This is a $O()$ solution in terms of time and $O()$ solution in terms of space.

<br>

```cpp
#include <unordered_map>
#include <string>
#include <algorithm>
#include <vector>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> string_to_anagrams;
        for(const auto& str : strs){    //n
            std::string temp{str};
            std::sort(temp.begin(), temp.end());    //mlogm
            string_to_anagrams[temp].push_back(str);
        }

        std::vector<std::vector<std::string>> res;
        for(const auto& pair : string_to_anagrams){ //n
            res.push_back(pair.second);
        }

        return res;
    }
};
```

- This has a quasi-quadratic $O(n * mlog(m))$ time complexity, where $n$ is the number of strings in the input vector and $m$ is the average length of each string.
- This has linear $O(m*n)$ space complexity, where $m$ is the number of unique anagrams in the input vector i.e. the space occuiped by the keys of the map and $n$ is the space occupied by the vector (value of the map) in the worst case all the strings could be anagrams.

<br>
<br>

## Notes

- Checkout how to use the std::sort function.
- How does std::sort sort the strings containing ascii? //REVIEW

<br>
<br>

## Resources

<br>
<br>
