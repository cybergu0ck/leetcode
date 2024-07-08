# Two Sum II - Input Array is Sorted

Medium level problem on leetcode.

<br>
<br>

## Description

Find it [here] (https://rebrand.ly/e3bo9ay).

<br>
<br>

## Solution

<br>

### Brute Force

- $O(n)$ solution using hash map.

    ```py
    class Solution:
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
            track = dict()
            for index, value in enumerate(numbers):
                needed = target - value
                if(needed in track):
                    return [track[needed],index+1]
                else:
                    track[value] = index+1
    ```



<br>

### Efficient Solution

- This is a $O(log(n))$ solution.
- Using binary search algorithm along with two pointer technique.

    ```py
    class Solution:
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
            l = 0
            r = len(numbers)-1
        
            while numbers[l] + numbers[r] != target:
                addition = numbers[l] + numbers[r]
                if addition < target:
                    l += 1
                else:
                    r -= 1
            return [l+1, r+1]
    ```

<br>
<br>

## Resources

<br>
<br>
