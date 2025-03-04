# 11. Container With Most Water

Medium [level question on leetcode](https://leetcode.com/problems/container-with-most-water/description/).

<br>
<br>
<br>

## Clarifications

<br>
<br>
<br>

## Test Cases

| Case | Input               | Output |
| ---- | ------------------- | ------ |
|      | [1,8,6,2,5,4,8,3,7] | 49     |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute Force

```py

```

```cpp

```

<br>

#### Explanation

Try every possible combination of two lines and determine the maximum area.

<br>

#### Complexity Analysis

- Time Complexity : This is a quadratic, $O(n^2)$ solution in terms of time, where $n$ is the size of the input array.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

### Linear Solution

```py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_area = 0

        while (l <r):
            area = (r-l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1

        return max_area
```

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() -1;
        int max_area = 0;

        while(l < r){
            int area = (r-l) * std::min(height[l], height[r]);
            max_area = std::max(max_area, area);

            if(height[l] < height[r]){
                l += 1;
            }
            else{
                r -= 1;
            }
        }
        return max_area;
    }
};
```

<br>

#### Explanation

Utilize two pointer approach by starting from opposite ends, update the pointer which has less height value.

Objective is to maximize the area (area = length \* breadth). To maximise the length component, we start with two pointers at opposite ends. For any two lines, the line with the lesser height must to chosen as breadth in area calculation. The pointers are updated based on the line with lesser height i.e. the pointer pointing to the line with less height is updated while the other is kept the same.

<br>

#### Complexity Analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is size of the input array.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
