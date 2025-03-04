# 191. Number of 1 Bits

Easy [level question on leetcode](https://leetcode.com/problems/number-of-1-bits/description/).

<br>
<br>
<br>

## Clarifications

What is the largest possible integer?

- $1 \le n \le 2^{31} - 1$. Which means the computer uses 32 bits.

<br>
<br>
<br>

## Test cases

| Case | Input      | Output |
| ---- | ---------- | ------ |
|      | 11         | 3      |
|      | 2147483645 | 30     |

<br>
<br>
<br>

## Solution

<br>
<br>

### Logarithmic solution

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

<br>

#### Explanation

Use right shift operator to get the LSB and then use bitwise AND operator with 1.

- First, check if the LSB is set by using bitwise and operator and 1 and initialise the res variable accordngly.
- Until the integer is valid (greater than 0), perform right shifting to get new lsb.
- In the same iteration, check if the new lsb is set using the bitwise and operator.s

<br>

#### Complexity analysis

- Time Complexity : This is a logarithmic, $O(log(n))$ solution in terms of time, where $n$ is the input integer.

  - The while loop will run as many times as the number of bits in the binary representation of the integer. An integer $n$ will have $log(n)$ number of bits.

- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>

#### Mathematical implementation

```py
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            if n%2 == 1:  #same as performing bitwsise and with 1
                res += 1
            n = n // 2    #same as right shifting by 1

        return res
```

- `if n%2 == 1` checks if lsb is 1. Similar to `n & 1`.
- `n = n // 2 ` right shifts the bits by 1. Similar to `n = n >> 1`.

<br>
<br>

### Constant time solution

```py

```

```cpp
#include <bitset>
#include <string>

class Solution {
public:
    int hammingWeight(int n) {
        std::bitset<32> binary_ip = n;  //O(1)
        std::string str_ip = binary_ip.to_string(); //O(1)as the bitset has 32 bits
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

<br>

#### Explanation

Create a string of the 32 bit bitset, created from the input integer. iterate over the 32 characters and check if they are '1'.

<br>

#### Complexity analysis

- Time Complexity : This is a constant, $O(1)$ solution in terms of time. The loop runs 32 times.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Know how to use the right shift operator.
- Know how to use the bitwise and operator.
- `if n%2 == 1` checks if lsb is 1. Similar to `n & 1`.
- `n = n // 2 ` right shifts the bits by 1. Similar to `n = n >> 1`.

Python :

- Know about python's `bin` function and it's `count` method. The following has $O(log(n))$ time complexity.

  ```py
  class Solution:
      def hammingWeight(self, n: int) -> int:
          binary = bin(n)  #log(n)
          return binary.count('1')  #log(n)
  ```

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
