# 238. Product of Array Except Self

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/product-of-array-except-self/description/).

<br>
<br>

## Test Cases

- The solution is not driven by test cases.

<br>
<br>

## Solution

<br>

### Brute Force

- The brute force solution will be quadratic $O(n^2)$ as it involves nested iterations.

<br>

### Linear Solution

```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prepare the preffix array
        preffix = []
        premul = 1
        for i in range(len(nums)):
            preffix.append(premul)
            premul *= nums[i]

        #prepare the suffix array
        suffix = []
        postmul = 1
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = postmul
            postmul *= nums[i]

        #multiply the corresponding indixes to get the answer
        answer = []
        for i in range(len(nums)):
            answer.append(preffix[i]*suffix[i])
        return answer
```

- The solution uses prefix and suffix arrays to compute the product of all elements except the current element in the input array.

  - `preffix` array is formed using nums, where preffix[i] is the product of all the elements to the left of `nums[i]`.
  - `suffix` array is formed using nums, where suffix[i] is the product of all tthe elements to the right of `nums[i]`.
  - Element wise multiplication of these two arrays yields the `answer`.

- This is a linear $O(n)$ solution in terms of time.
- This is a linear $O(n)$ solution in terms of space, as the length of result array will be equal to the number of elements in the input array.

<br>

```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prepare the preffix array
        preffix = []
        premul = 1
        for i in range(len(nums)):
            preffix.append(premul)
            premul *= nums[i]

        #multiply the suffixes directly to the preffix
        postmul = 1
        for i in range(len(nums)-1,-1,-1):
            preffix[i] *= postmul
            postmul *= nums[i]

        return preffix
```

- We can get rid of the preparing suffix array by directly multiplying the element to the preffix array itself.

<br>

```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        #left pass
        premul = 1
        for i in range(len(nums)):
            ans.append(premul)
            premul *= nums[i]

        #right pass
        postmul = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= postmul
            postmul *= nums[i]

        return ans
```

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer;
        int premul{1};
        for(int i = 0; i<nums.size(); ++i){
            answer.push_back(premul);
            premul *= nums[i];
        }

        int postmul{1};
        for(int i = nums.size()-1; i>-1; --i){
            answer[i] *= postmul;
            postmul *= nums[i];
        }

        return answer;
    }
};
```

- Utilise two running products for left pass and right pass iterations.

  - The algorithm computes the product of all elements except the current element by maintaining two running products: a prefix product and a suffix product. The prefix product is computed from left to right, and the suffix product is computed from right to left. The final result is obtained by multiplying the corresponding prefix and suffix products for each element.

- This is a linear $O(n)$ solution in terms of time.
- This is a linear $O(n)$ solution in terms of space, as the length of result array will be equal to the number of elements in the input array.

<br>

<br>
<br>

## Notes

- In Python, the `insert` method of list is a $O(n)$ opeartion.

<br>
<br>

## Resources

<br>
<br>
