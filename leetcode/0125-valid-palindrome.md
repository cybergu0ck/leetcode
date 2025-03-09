# 125. Valid Palindrome

Easy [level question on leetcode](https://leetcode.com/problems/valid-palindrome/description/).

<br>
<br>
<br>

## Clarifications

- Can the string be empty and what is the expected result for empty string?

  - String is not empty

- It is mentioned that the string can contain alphanumeric and non-alphanumeric characters.

<br>
<br>
<br>

## Test cases

| Case | Input                           | Output |
| ---- | ------------------------------- | ------ |
|      | A man, a plan, a canal: Panama" | true   |
|      | "race a car"                    | false  |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ""
        for c in s: #O(n)
            if c.isalnum():
                alphanumeric += c.lower()

        forward = alphanumeric
        backward = alphanumeric[::-1]  #O(n)
        if(forward == backward): #checking the strings is O(n)
            return True
        else:
            return False

```

```cpp

```

<br>

#### Explanation

Create a lower case alphanumeric string out of the input string and check if it is equal to its reverse.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the size of the input string.

  - Note that comparing two strings is $O(n)$.

- Space Complexity : This is a linear, $O(m)$ solution in terms of space, where $m$ is the number of alphanumeric characters in the input string.

<br>
<br>

### Linear solution

```py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while(left < right):
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
```

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int left{0};
        int right = s.length()-1;

        while(left < right)
        {
            if(!std::isalnum(s.at(left)))
            {
                left+=1;
            }
            else if(!std::isalnum(s.at(right)))
            {
                right-=1;
            }
            else if(std::tolower(s.at(left)) != std::tolower(s.at(right)))
            {
                return false;
            }
            else
            {
                left += 1;
                right -= 1;
            }
        }
        return true;
    }
};
```

<br>

#### Explanation

Use left and right pointers from two ends of the string and check the characters.

- Initialise the left pointer to point at the first character of the string and right character to the last character of the string.
- If the characters are non-alphanumeric then update the pointes.
- Check the charactes after changing the case to lowercase and return the result.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is size of the input string.
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

- The function to check if a character is alphanumeric in Python is `isalnum()`.
- The function to convert upper case to lower case in Python is `lower()`.
- Use slicing to reverse a string i.e. `string[::-1]`.

C++:

- The function to check if a character is alphanumeric in C++ is `std::isalnum()`.
- The function to convert upper case to lower case in C++ is `std::tolower()`.
- Use `std::reverse` to reverse a string.

  ```cpp
  #include <iostream>
  #include <string>
  #include <algorithm>

  int main() {
      std::string str = "hello";
      std::reverse(str.begin(), str.end());
      std::cout << str << std::endl; // Output: olleh
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
