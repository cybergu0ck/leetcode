# Strings

### 1.1 Is Unique

_Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?_

- Follow ups:
- Test cases:

  - "abc"
  - "a"
  - "aa"
  - ""

- A linear time solution ($O(n)$) using unordered_map.

  ```cpp
  #include <string>
  #include <unordered_map>

  bool is_unique(std::string str){
      std::unordered_map<char, int> char_to_freq;

      for(char c: str){
          auto it = char_to_freq.find(c);
          if(it != char_to_freq.end()){
              return false;
          }
          char_to_freq[c] = 1;
      }
      return true;
  }
  ```

- A quadratic time solution ($O(n^2)$) using nested loops.

  ```cpp
  bool is_unique(std::string str){
      for(int i=0; i < str.size(); ++i){
          for(int j=i+1; j < str.size(); ++j){
              if(str[i] == str[j]){
                  return false;
              }
          }
      }
      return true;
  }
  ```

<br>

### 1.2 Check Permutation

_Given two strings, write a method to decide if one is a permutation of the other._

- The problem statement is essentially asking if the two strings are anagrams of each other.

- Follow ups:

  - What kind of characters are present in the strings? only alphabets or any ascii?

- Test cases:

  - "" and "", true.
  - "a" and "a", true.
  - "ab" and "ba", true.
  - "ab" and "ac", false.
  - "abc" and "xyz", false.

- This is a log-linear time solution ($O(n*log(n))$) using sorting algorithm.

  ```cpp
  #include <string>
  #include <unordered_map>
  #include <algorithm>

  bool check_permutation(std::string str1, std::string str2){
      std::sort(str1.begin(), str1.end());
      std::sort(str2.begin(), str2.end());

      if(str1 == str2){
          return true;
      }
      else{
          return false;
      }
  }
  ```

- A linear time solution ($O(n)$) using a vector.

  ```cpp
  #include <string>
  #include <unordered_map>
  #include <algorithm>
  #include <vector>

  bool check_permutation(std::string str1, std::string str2){
      std::vector<int> char_freq(256,0);

      for(auto c: str1){
          ++char_freq[c];
      }

      for(auto c:str2){
          --char_freq[c];
          if(char_freq[c] < 0){
              return false;
          }
      }
      return true;
  }
  ```

<br>

### 1.3 URLify

_Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string._(Note: If implementing in Java, please use a character array so that you can perform this operation in place.)

- Follow up
  - In place manipulation must be implemented?
