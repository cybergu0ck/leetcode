# Number of 1 Bits

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/number-of-1-bits/description/).

- Some good follow ups are:
  - How to handle greater than 32 bits.
  - How to handle negative integers.

<br>
<br>

## Test Cases

This is not a test case driven question.

<br>
<br>

## Solution

<br>

### Linear Solution

```py
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        return binary.count('1')
```

```cpp
#include <bitset>
#include <string>

class Solution {
public:
    int hammingWeight(int n) {
        std::bitset<32> binary_ip = n;  //O(n)
        std::string str_ip = binary_ip.to_string(); //O(n)
        int res{0};
        for(auto c : str_ip){
            if(c == '1'){
                ++res;
            }
        }
        return res;
    }
};
```

- The algorithm used is
  1. Create a bitset using the input integer.
  1. Create a string using the bitset.
  1. Iterate over each character of the string and count the number of '1'.
- This is a linear $O(n)$ solution in terms of time, where $n$ is the number of bits in the input integer.
- This is a constant $O(32)$ solution in terms of space.

<br>

### Efficient Solution

```py
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = n & 1
        while n > 0:
            n = n >> 1
            res += n & 1
        return res
```

```cpp
class Solution {
public:
    int hammingWeight(int n) {
        int res = n & 1;
        while(n > 0)
        {
            n = n >> 1;
            res += n & 1;
        }
        return res;
    }
};
```

- This is a linear $O(n)$ solution in terms of time, where $n$ is the number of bits. Therefore for a given bit of integer (say 32 bit integer), this can be considered as a constant time solution.
- This is a constant $O(1)$ solution in terms of space.
- A different variation using the same logic, however I would prefer the above one as for a smaller integer, the below code will unnecessarily execute more iterations.

  ```cpp
  class Solution {
  public:
      int hammingWeight(int n) {
          int res {0};
          for(int i=0; i <32; ++i){
              if((n >> i) & 1){
                  ++res;
              }
          }
          return res;
      }
  };
  ```

<br>
<br>

## Notes

- For Python:
  - `bin` function.
- For C++:
  - Usage of "right shift operator" and "bitwise and" operator.
  - Know how to create a std::bitset.
  - Know about `to_string` method of std::bitset.

<br>
<br>

## Resources

<br>
<br>
