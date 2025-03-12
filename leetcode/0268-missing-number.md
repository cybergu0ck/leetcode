# 268. Missing Number

Easy [level question on leetcode](https://leetcode.com/problems/missing-number/description/).

<br>
<br>
<br>

## Clarifications

- The question mentions that the input array contains "n" distinct numbers but the range mentioned is [0,n], which has "n+1" elements. Hence there exists a missing number always.

<br>
<br>
<br>

## Test cases

| Case             | Input   | Output |
| ---------------- | ------- | ------ |
| Simple case      | [3,0,2] | 1      |
| Only unique case | [0,1]   | 2      |

- The above test cases cover all the test cases.

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        unique_set = set(nums)

        for i in range(len(nums)+1):  # +1 takes care of the above mentioned unique case
            if i not in unique_set:
                return i
```

```cpp

```

<br>

#### Explanation

Iterate from 0 to n and check if the value is in the set, return the value that is not present.

- Create a set from the input array.
- Iterate over the range from 0 to n (inclusive of n) and check if the value is in the set.
- A value exits in the iteration that will not be present in the set, return that.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is size of the input array.
- Space Complexity : This is a linear, $O(n)$ solution in terms of space, where $n$ is size of the input array.

  - The size of the set will be one less than the size of the input array, which is still linear.

<br>
<br>

### Linear solution

```py
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        entire_sum = sum([i for i in range(len(nums)+1)])
        given_sum = sum(nums)

        return entire_sum - given_sum
```

```cpp

```

<br>

#### Explanation

Return the sum of the entire range minus the sum of given range.

- Note that the range mentioned in the question is [0,n]. Hence range(len(nums)+1) makes sure that "n" is included.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is size of the input array.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

#### Implementation using binary operator

```py
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        res = 0
        for num in nums:
            res ^= num
        for i in range(length+1):
            res ^= i
        return res
```

Using the properties of binary XOR.

- `A XOR 0 = A`
- `A XOR A = 0`
- `A XOR B XOR A = B`

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Note and memorise the properties of binary xor mentioned above.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
