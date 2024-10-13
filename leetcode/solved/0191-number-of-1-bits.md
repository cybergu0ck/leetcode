# Number of 1 Bits

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/number-of-1-bits/description/).

- Some good follow ups are:

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

```

```cpp

```

- This is a $O()$ solution in terms of time, where $ $ is .
- This is a $O()$ solution in terms of space, where $ $ is .

<br>
<br>

## Notes

- Know how to create a std::bitset.
- Know about `to_string` method of std::bitset.

<br>
<br>

## Resources

<br>
<br>
