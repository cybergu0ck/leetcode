# 242. Valid Anagram

Easy [level question on leetcode](https://leetcode.com/problems/valid-anagram/description/).

<br>
<br>
<br>

## Clarifications

- Confirm the definition of an anagram.

  - An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

- Does the strings contain only alphabets?

  - Yes

<br>
<br>
<br>

## Test cases

| Case    | Input                        | Output |
| ------- | ---------------------------- | ------ |
| Valid   | s = "anagram", t = "nagaram" | true   |
| Invalid | s = "rat", t = "car"         | false  |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force, linearithmic

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        if(s == t):
            return True
        else:
            return False
```

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());

        if(s == t)
            return true;
        else
            return false;
    }
};
```

<br>

#### Explanation

Sort the strings based on the characters and then check if they are same.

<br>

#### Complexity analysis

- Time Complexity : This is a linearithmic, $O(n * log(n))$ solution in terms of time, where $n$ is number of characters in the input string.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

### Linear solution

```py
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_to_freq = defaultdict(int)

        for c in s:
            char_to_freq[c] += 1

        for c in t:
            char_to_freq[c] -= 1

        for key in char_to_freq:
            if(char_to_freq[key] != 0):
                return False
        return True
```

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char,int> char_to_freq;

        for(auto ch : s){
            char_to_freq[ch]++;
        }
        for(auto ch : t){
            char_to_freq[ch]--;
        }

        for(auto pair : char_to_freq){
            if(pair.second != 0)
                return false;
        }
        return true;
    }
};
```

<br>

#### Explanation

Count character frequencies in a map for the first string, decrement the values of the same map for the second; anagrams have all zero counts.

- Utilize a map with keys as characters and values as frequencies, iterate over the characters of first string and increment the values in the map. Iterate over the characters of the second string and decrement the values. Finally, iterate over the map, it should have all the values as zeros if the strings are anagram.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the maximum number of characters in the input string.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.
  - It is mentioned that all the characters are alphabets, hence the size of the map would be at max 26.

<br>

#### Intuitive solution

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char,int> char_to_freq_s;
        std::unordered_map<char,int> char_to_freq_t; //use of additional map!

        for(auto ch : s){
            char_to_freq_s[ch]++;
        }
        for(auto ch : t){
            char_to_freq_t[ch]++;
        }

        if(char_to_freq_s == char_to_freq_t)
            return true;
        else
            return false;
    }
};
```

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::array<int, 26> freq;

        for(auto ch : s){
            freq[ch - 'a']++;
        }

        for(auto ch : t){
            freq[ch - 'a']--;
        }

        for(auto num : freq){
            if(num != 0)
                return false;
        }
        return true;
    }
};
```

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Learn about ascii

Python :

- Know how to use defaultdicts. It is imported from collections package.

  ```py
  from collections import defaultdict

  map = defaultdict(int)
  ```

- `ord` returns the ASCII value of the parameter.

C++:

- Learn about stl arrays.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
