# Longest Substring Without Repeating Characters

medium level problem on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

<br>
<br>

## Solution

<br>

### Brute Force

- $O(n^2)$ solution.

  ```py
  class Solution:
      def lengthOfLongestSubstring(self, s: str) -> int:
          longest = 0
          for i, v in enumerate(s):
              longest = max(longest, 1)
              new = v
              for w in s[i + 1 :]:
                  if w not in new:
                      new += w
                  else:
                      longest = max(longest, len(new))
                      break
              longest = max(longest, len(new))
          return longest


  answer = Solution()
  print(answer.lengthOfLongestSubstring("abcabcbb"))
  ```

<br>

### Efficient

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
       std::set<char> unique_characters;  //Compare time complexity with unordered set

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

- The approach here is to use "Sliding Window" with "set" data structure.

- This has linear $O(n)$ time complexity $O(n)$ space complexity.
  - This is not $O(n^2)$ time complexity because each character is added and removed only once as the left pointer moves only forward and not backward.

<br>
<br>

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        char_indices = [-1 for num in range(128)]

        for right in range(len(s)):
            if(char_indices[ord(s[right])] >= left):
                left = char_indices[ord(s[right])] + 1 #+1 because we don't want to include the repeat character
            res = max(res, right - left + 1)
            char_indices[ord(s[right])] = right

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

- The approach here is to use "Sliding Window" with "vector" data structure and is more efficient than the set and map counterparts.
  - Accessing a set by index is $O(n)$ while that for a vector is $O(1)$.
- This has linear $O(n)$ time complexity $O(n)$ space complexity.

<br>
<br>

## Notes

- In average case, unorderd_set is better than set in terms of time complexity (not in worst case where there is a hash collision).
- For accessing by index, vectors are always better than maps and sets.
- In Python, `ord` function is used to get the ascii value for a character and `chr` function is used to get the character for a given ascii value.

  ```py
  print(ord('c'))  #character to ascii value
  print(chr(99))   #asci to character value
  ```

- In C++,

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

## Resources

<br>
<br>
