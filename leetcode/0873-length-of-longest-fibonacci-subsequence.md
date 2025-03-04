# Length of longest fibonacci subsequence

Medium [level question on leetcode](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/).

<br>
<br>
<br>

## Clarifications

1. Is the minimum size of the input array equal to 3.

   - Yes, it is.

2. Confirm the definition of subsequence.

   - Subsequence is a part of the array in which the elements maintain their relatice order but not necessarily contigiuous. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

3. Does the input array have duplicate values?

   - It is mentioned that array is "strictly increasing", then by defintion it means that the array will not have duplicate values!

<br>
<br>
<br>

## Test Cases

| Case | Input               | Output                                    |
| ---- | ------------------- | ----------------------------------------- |
|      | [1,2,3,4,5,6,7,8]   | 5; i.e. [1,2,3,5,8]                       |
|      | [1,3,7,11,12,14,18] | 3; i.e. [1,11,12], [3,11,14] or [7,11,18] |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute Force

```py
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res = 0
        for first in range(len(arr)):
            for second in range(first+1, len(arr)):
                fib = [arr[first], arr[second]]
                for cur in range(second+1, len(arr)):
                    if(arr[cur] == fib[-1] + fib[-2]):
                        fib.append(arr[cur])
                        res = max(res, len(fib))
        return res
```

```cpp

```

<br>

#### Explanation

A minimum of two numbers are required for the Fibonacci subsequence. Try every possible array variation for the first two values of the fibonacci subsequence. Iterate over the reamining elements in the input array and build the fiboncacci subsequence and determine the longest subsequence.

<br>

#### Complexity Analysis

- **Time Complexity**: This is a cubic, $O(n^3)$ solution in terms of time, where $n$ is size of the input array .
- **Space Complexity**: This is a linear, $O(n)$ solution in terms of space, where $n$ is the size of the actual fibonacci subsequence.

<br>
<br>

### Efficient Solution

```py
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res = 0
        arr_len = len(arr)
        num_set = set(arr)  #O(n)

        for first in range(arr_len):
            for second in range(first+1, arr_len):
                prev_value = arr[first]
                cur_value = arr[second]
                next_value = prev_value + cur_value
                length = 2
                while(next_value in num_set):
                    prev_value = cur_value
                    cur_value = next_value
                    next_value = prev_value + cur_value
                    length += 1
                    res = max(res, length)
        return res
```

```cpp
class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        int res = 0;
        int arr_len = arr.size();
        std::unordered_set<int> num_set(arr.begin(), arr.end());

        for(int first = 0; first < arr_len; ++first ){
            for(int second = first + 1; second < arr_len; ++second){
                int prev_value = arr[first];
                int cur_value = arr[second];
                int next_value = prev_value + cur_value;
                int length = 2;

                while(num_set.find(next_value) != num_set.end()){
                    prev_value = cur_value;
                    cur_value = next_value;
                    next_value = prev_value + cur_value;
                    length += 1;
                    res = std::max(res, length);
                }
            }
        }
        return res;

    }
};
```

<br>

#### Explanation

Begin with all variations for first two numbers for the fib subsequence and then check if the subsequent number is present in the set.

<br>

A minimum of two numbers are required for the Fibonacci subsequence. Try every possible array variation for the first two values of the fibonacci subsequence. Instead of iterating over the remaining values in the input array, check if the next fibonaccci value is present in the set created using the input array and then determine the longest subsequence.

- Store the length of the input array in a variable as it is used in range functions in two loops.
- Create a set from the input array to efficiently perform the search.

<br>

#### Complexity Analysis

- **Time Complexity**: This is a cubic, $O(n^2*log(m))$ solution in terms of time, where $n$ is size of the input array and $m$ is the largest number in the array .

  - Fibonacci numbers grow exponentially, a sequence that stays within a maximum value of $10^9$ can have at most 43 terms. This is because the Fibonacci sequence increases so rapidly that it reaches $10^9$ in at most 43 steps. As a result, the inner loop can run at most 43 times, meaning it runs in $O(log(m))$ time, where m is the largest number in array.

  - Note: Some might consider the complexity to be $O(n^3)$, but that assumption holds only if we consider the worst case where the sequence length is $O(n)$. However, since Fibonacci numbers grow exponentially, the maximum sequence length is actually bounded by $O(log(m))$ rather than $O(n)$.

- **Space Complexity**: This is a linear, $O(n)$ solution in terms of space, where $n$ is the size of the set formed from the input array.

<!-- TODO - Understand the DP solution that has O(n2) -->

<br>
<br>
<br>

## Follow ups

1. Return the longest fibonacci subsequence the actaul array. <!-- TODO -->

<br>
<br>
<br>

## Notes

1. Know how to create a set from a vector in C++!
1. Know about set's `find` method in C++!
1. Understand the difference between unordered set and set in stl.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
