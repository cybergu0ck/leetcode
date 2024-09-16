# 125. Valid Palindrome

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/valid-palindrome/description/).

- Some good follow ups are:

<br>
<br>

## Solution

<br>

### Brute Force

```py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non alpha numeric characters; O(n)
        alphanumeric_string = ""
        for char in s:
            if char.isalnum():
                alphanumeric_string += char.lower()

        #check if the string is a palindrome; O(n)
        left = 0
        right = len(alphanumeric_string)-1

        while(left <= right):
            if alphanumeric_string[left] == alphanumeric_string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
```

- This is a $O(n)$ solution in terms of time and $O(1)$ solution in terms of space.

<br>

### Efficient Solution

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

- This is a $O(n)$ solution in terms of time and $O(1)$ solution in terms of space.

<br>

### Ideal Solution

```py

```

- This is a $O()$ solution in terms of time and $O()$ solution in terms of space.

<br>
<br>

## Notes

- The function to check if a character is alphanumeric in Python is `.isalnum()`.
- The function to check if a character is alphanumeric in C++ is `std::isalnum()`.

- The function to convert upper case to lower case in Python is `.lower()`.
- The function to convert upper case to lower case in C++ is `std::tolower()`.

<br>
<br>

## Test Cases

<br>
<br>

## Resources

<br>
<br>
