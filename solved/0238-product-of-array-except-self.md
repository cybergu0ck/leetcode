# 238. Product of Array Except Self

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/product-of-array-except-self/description/).

<br>
<br>

## Solution

<br>

### Brute Force

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>

### Efficient Solution

- The following has $O(n)$ time complexity $O(n)$ space complexity.

  ```py
  class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1]
        for index in range(len(nums)-1):
            product = left_products[-1]*nums[index]
            left_products.append(product)

        right_products = [1]
        for index in range(len(nums)-1,0,-1):
            product = right_products[-1]*nums[index]
            right_products.append(product)  
        right_products = right_products[::-1]

        res = []
        for i in range(len(nums)):
            res.append(left_products[i] * right_products[i])
        
        return res
  ```


<br>

### Ideal Solution

- The following has $O(n)$ time complexity $O(1)$ space complexity.

  ```py
  class Solution:
      def productExceptSelf(self, nums: List[int]) -> List[int]:
          res = [1]*len(nums)

          premul = nums[0]
          for index in range(1, len(nums)):
              res[index] = premul
              premul *= nums[index]

          postmul = 1
          for index in range(len(nums)-1,-1,-1):  
              res[index] *= postmul
              postmul *= nums[index]
          
          return res
  ```

<br>
<br>

## Notes

- Initialise the res array, left pass on it using premul variable and then overwrite over it with right pass using postmul.

<br>
<br>

## Test Cases

- The solution is not driven by test cases.

<br>
<br>

## Resources

<br>
<br>
