# 3. Longest Substring Without Repeating Characters

Medium [level question on leetcode](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/).

<br>
<br>
<br>

## Clarifications

- Clarify the definition of a substring.

  - A substring is a contigious non-empty sequence of characters within the string.

- Can the input string be empty? If yes what is the expected result?

  - It can be empty string and the result should be 0.

- What kind of characters are present in the input string?

  - The string consists of English letters, digits, symbols and spaces.

<br>
<br>
<br>

## Test cases

| Case                                                              | Input  | Output |
| ----------------------------------------------------------------- | ------ | ------ |
| Empty string                                                      | ""     | 0      |
| All unique characters                                             | "abc"  | 3      |
| Repeated character is present at the begining (a is first in abc) | "abca" | 1      |
| Repeated character is present in between (b is in between abc)    | "abcb" | 3      |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        for right in range(len(s)):
            while(s[right] in s[left:right]):
                left += 1
            res = max(res, right - left +1)
        return res
```

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res{0};
        int left{0};
        for(int right = 0; right < s.length(); right++)
        {
            while(s.substr(left, right-left).find(s[right]) != std::string::npos)
            {
                left+=1;
            }
            res = std::max(res, right-left+1);
        }
        return res;
    }
};
```

<br>

#### Explanation

Use sliding window technique without storing characters in a data structure.

- Initialise a left pointer to point to the start index of the substring.
- In a nested loop, increment the left pointer until the substring is unique and update the result.

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(n^2)$ solution in terms of time, where $n$ is the size of the input string.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

### Linear solution

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_characters = set()
        res = 0
        left = 0

        for right in range(len(s)):
            while(s[right] in unique_characters):
                unique_characters.remove(s[left])
                left += 1
            unique_characters.add(s[right])
            res = max(res, right-left+1)

        return res
```

```cpp
#include <set>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
       int res{0};
       int left{0};
       std::unordered_set<char> unique_characters;

       for(int right=0; right<s.length();++right)
       {
           while(unique_characters.find(s[right]) != unique_characters.end())
           {
                unique_characters.erase(s[left]);
                left += 1;
           }
           unique_characters.insert(s[right]);
           res = std::max(res, right-left+1);
       }
       return res;
    }
};
```

<br>

#### Explanation

Use sliding window technique and store the characters in a set.

- Initialise a left pointer to point to the start index of the substring.
- While iterating over the string if the character is not present in the set, add it to the set.
- While iterating over the string if the character is present in the set, keep removing the character pointed by the left pointer and increment the left pointer.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is size of the input string.

  - This is not $O(n^2)$ time complexity because each character is added and removed only once in the set, as the left pointer moves only forward and not backward.

- Space Complexity : This is a linear, $O(m)$ solution in terms of space, where $m$ is number of unique characters in the input string.

<br>
<br>

### Linear solution with space

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        char_indices = [-1 for num in range(128)]

        for right in range(len(s)):
            if(char_indices[ord(s[right])] >= left):
                left = char_indices[ord(s[right])] + 1 #+1 because we don't want to include the repeat character
            char_indices[ord(s[right])] = right
            res = max(res, right - left + 1)

        return res
```

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res{0};
        int left{0};
        std::vector<int> char_index(128,-1); //there are 128 ASCII values.

        for(int right=0; right < s.length(); right++)
        {
            if(char_index[s[right]] >= left)
            {
                left = char_index[s[right]] + 1; //+1 as we donot want to include the repeat
            }
            char_index[s[right]] = right;
            res = std::max(res, right - left + 1);
        }
        return res;
    }
};
```

<br>

#### Explanation

Use sliding window technique and use a vector to store the index of the characters.

- Initialise a left pointer to point to the start index of the substring and a vector of 128 (since we have 128 ascii characters) values allinitialised to -1.
- Iterate over the string, use the ascii of the character as the index in the vector.
  - If the value at the index is greater than the left pointer, it means that the character is repeated in between the string (ex: abcb, b is in abc)hence update the left pointer using the value in the vector!
    -Update the vector to store the last index of the characters.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is size of the input string.

  - This is not $O(n^2)$ time complexity because each character is added and removed only once in the set, as the left pointer moves only forward and not backward.

- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

Python :

- Using a vector of fixed size will save space instead of using map, this is ideal when the elements are known prior.

- `ord` function is used to get the ascii value for a character and `chr` function is used to get the character for a given ascii value.

  ```py
  print(ord('c'))  #character to ascii value
  print(chr(99))   #asci to character value
  ```

C++ :

- The ascii value and corresponding character is obtained by casting.

  ```cpp
  #include <iostream>

  int main() {
      int asci_value = 'c';
      std::cout << asci_value << std::endl;  //99

      char char_value = 99;
      std::cout << char_value << std::endl;  //c
      return 0;
  }
  ```

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
