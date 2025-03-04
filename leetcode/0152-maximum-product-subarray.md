# Maximum Product Subarray

Medium level [question on leetcode](https://leetcode.com/problems/maximum-product-subarray/description/).

<br>
<br>
<br>

## Clarifications:

- Confirm the definition of a [subarray](#notes).
- Can the input array be empty?
  - No

<br>
<br>
<br>

## Test Cases

| Case                               | Input         | Output |
| ---------------------------------- | ------------- | ------ |
| Even number of negative values     | [2,3,-2,4,-2] | 96     |
| Odd number of negative values      | [2,3,-2,4]    | 6      |
| Containing numbers that are zeroes | [-3,0,1,-2]   | 1      |
| Edge cases                         | [0,2]         | 2      |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute Force

```py
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod_max = float('-inf')
        for i in range(len(nums)):
            prod = nums[i]
            for j in range(i,len(nums)):
                if i != j:
                    prod *= nums[j]
                prod_max = max(prod_max, prod)
        return prod_max
```

```cpp

```

<br>

#### Explanation

Determine the maximum product of subarrays by iterating through every possible subarray.

<br>

#### Complexity Analysis

- **Time Complexity**: This is a quadratic $O(n^2)$ solution in terms of time, where $n$ is the number of elements in the input array.
- **Space Complexity**: This is a constant $O(1)$ solution in terms of space.

<br>
<br>

### Linear Solution

```py
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod_max = float('-inf')
        prod_preffix = 1
        prod_suffix = 1
        for index in range(len(nums)):
            if prod_preffix == 0:
                prod_preffix = 1
            if prod_suffix == 0:
                prod_suffix = 1
            prod_preffix *= nums[index]
            prod_suffix *= nums[len(nums)-1-index]
            prod_max = max(prod_max, max(prod_preffix, prod_suffix))

        return prod_max
```

```cpp

```

<br>

#### Explanation

Determine the maximum product of subarrays by iterating through the array from both ends, leveraging the properties of negative numbers to form larger subarrays while treating zeros as boundaries that reset the product calculation.

1. **Avoiding Small Subarrays**:

   - The intent is to avoid checking every possible subarray. Instead, we concentrate on larger ones, as they are more likely to yield a higher product.

2. **Role of Negative Numbers**:

   - If a subarray has an **even** number of negative numbers, the product will be **positive**.
   - If it has an **odd** number of negative numbers, the product will be **negative**.
   - A single negative number can split the array into two parts based on its position.
     - **Example**: Given the input array `[1, -2, 3]`, we can split it as `[1]` and `[-2, 3]` (Case 1) or as `[1, -2]` and `[3]` (Case 2).
   - We need to check the maximum product in these subarrays as well as the product of the entire input array.

3. **Iterative Approach**:

   - We iterate through the array from the **beginning** to cover cases like the first subarrays in Case 1 and Case 2.
   - We also iterate from the **end** to cover cases like the second subarrays in Case 1 and Case 2.

4. **Handling Zeros**:

   - Zeros are special cases because they reset the product to one. Whenever we encounter a zero, we end the current subarray and start a new one.

<br>

#### Complexity Analysis

- **Time Complexity**: This is a linear \(O(n)\) solution, where \(n\) is the number of elements in the input array.
- **Space Complexity**: This is a constant \(O(1)\) solution in terms of space.

<br>
<br>
<br>

## Follow up

#TODO - Find the actual subarray that has the maximum product.

<br>
<br>
<br>

## Notes

- _A **subarray** is a contigious non-empty sequence of elements within an array_.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
