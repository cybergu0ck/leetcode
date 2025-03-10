# 49. Group Anagrams

Medium [level question on leetcode](https://leetcode.com/problems/group-anagrams/description/).

<br>
<br>
<br>

## Clarifications

Q: Confirm the definition of an anagram.

- An anagram of a string is a string that has same number of and type of characters as that of the original string but rearranged differently.

Q: It is mentioned that the order in the output is not important.

Q: Can the input array be empty?

- No

Q: What kind of characters are present in the strings?

- Only lower case english letters.

<br>
<br>
<br>

## Test cases

| Case                                      | Input                                 | Output                                      |
| ----------------------------------------- | ------------------------------------- | ------------------------------------------- |
| list containing anagrams and non anagrams | ["eat","tea","tan","ate","nat","bat"] | [["bat"],["nat","tan"],["ate","eat","tea"]] |
| list containing single string             | ["aat"]                               | [["aat"]]                                   |
| list containing single empty string       | [""]                                  | [[""]]                                      |

- The above test cases should cover all the cases.

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uniqueid_to_anagrams = defaultdict(list)
        for string in strs: #O(n)
            uniqueid = ''.join(sorted(string))  #O(mlogm)
            uniqueid_to_anagrams[uniqueid].append(string)

        return list(uniqueid_to_anagrams.values())
```

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

<br>

#### Explanation

Use a map with the keys as the sorted version of the string.

- Initialise a map with values as arrays.
- Iterate over the input array containing the strings.
- Sort the string and use it as the unique key, append the original string to the value of the map.
- Return the list containing all the values of the map.

<br>

#### Complexity analysis

- Time Complexity : This is a quasi-quadratic, $O(n * mlog(m))$ solution in terms of time, where $n$ is the size of the input array and $m$ is the size of the longest string in the input array.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the number of anagrams present.

<br>
<br>

### Quadratic solution

```py
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uniqueid_to_anagrams = defaultdict(list)
        for string in strs:
            uniqueid = [0 for i in range(128)] #ascii is for 128 characters
            for c in string:
                uniqueid[ord(c) - ord('a')] += 1
            uniqueid_to_anagrams[tuple(uniqueid)].append(string)

        return list(uniqueid_to_anagrams.values())
```

```cpp

```

<!-- TODO - write the C++ version of this  -->

<br>

#### Explanation

Use a map with keys as unique encoding and values as the array of anagrams.

- Iterate over the input array of strings.
- For each string, create the unique encoding, a vector whose index correspongs to the ascii value and the elements represent the frequency.
- use the unique encoding as the key and append the original string to the array (value of the map)

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(n*m)$ solution in terms of time, where $n$ is size of the input array and $m$ is the size of the longest string.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is the number of unique anagrams in the input array.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

Know that sorting is generally $n*log(n)$.

<br>

Python :

- Know how defaultdicts with list values work.
- Know about `ord` function, which gives the ascii value of a character.
- Know that `sort` sorts inplace and `sorted` returns a list of sorted elements.
- Know how to use `join` method.
- Know that dictionaries cannot use list as keys but can use tuples.

C++:

- Know to use the `std::sort` for strings.

<!-- TODO - complete the C++ points here -->

<br>
<br>
<br>

## Resources

- Solution is same as [neetcode's](https://www.youtube.com/watch?v=vzdNOK2oB2E)

<br>
<br>
<br>
