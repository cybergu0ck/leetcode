# 3sum

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/3sum/).

<br>
<br>

## Solution

<br>

### Brute Force

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>

### Efficient Force

- The following has $O(n^2)$ time complexity $O(1)$ space complexity.

  ```py
  class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        num.sort()
        res = []
        for i, a in enumerate(num):
            if (i >0 and a == num[i -1]):
                continue
            l = i +1
            r = len(num)-1
            while (l < r):
                sum = num[i] + num[l] + num[r]
                if (sum > 0):
                    r -= 1
                elif (sum < 0):
                    l += 1
                else:
                    res.append([num[i], num[l], num[r]])
                    l +=1
                    while (num[l] == num[l-1] and l < r):
                        l+=1
        return res
  ```

  - The sorting takes $O(n*log(n))$ and there is a nested iteration happening which is $O(n^2)$, Hence the overall time complexity would be $O(n*log(n) + n^2)$

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>
<br>

## Notes

- Easier to solve after solving 2 sum and 2 sum II.

<br>
<br>

## Test Cases

There are two edge cases which are good to know

1. Say the input is [4,4,1,3,-4], after first iteration if the item is same as that of previous item (in this case 2nd item is same as 1st item i.e 4) then we can skip this one and move to the next one (in terms of left pointer).

2. Say the input is [1,-1,-1,4,0], we get the one favouring outcome in the first iteration itself, now if we increment the left pointer we see that it is same as when it was before (It was -1 initially, after increment aslo it is -1). We need to skip these also.

<br>
<br>

## Resources

<br>
<br>
