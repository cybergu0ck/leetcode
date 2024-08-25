# Two Sum

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/two-sum/description/).

<br>
<br>

## Solution

<br>

### Brute Force

- This is a $O(n^2)$ solution.

  ```py
  from typing import List

  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          for i, v in enumerate(nums):
              for j, w in enumerate(nums):
                  if i != j:
                      if v + w == target:
                          return [i, j]


  answer = Solution()
  print(answer.twoSum([2, 7, 11, 15], 9))

  # [0,1]
  ```

  ```cpp
  #include <vector>
  #include <unordered_map>
  #include <algorithm>

  class Solution {
  public:
      vector<int> twoSum(vector<int>& nums, int target)
      {
          std:vector<int> res;
          for(int i = 0; i < nums.size(); i++)
          {
              for(int j= i+1; j < nums.size(); j++)
              {
                  if(nums[i] + nums[j] == target)
                  {
                      res.push_back(i);
                      res.push_back(j);
                      break;
                  }
              }
          }
          return res;
      }
  };
  ```

<br>

### Efficient Solution

- This is a $O(n)$ solution, considering that the average-case time complexity to check if a key is present in a dictionary is $O(1)$.

  ```py
  from typing import List

  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          map = {}
          for index, value in enumerate(nums):
              needed = target - value
              if needed in map:
                  return [index, map[needed]]
              map[value] = index

  answer = Solution()
  print(answer.twoSum([2, 7, 11, 15], 9))
  # [0,1]
  ```

  ```cpp
  #include <vector>
  #include <unordered_map>
  #include <algorithm>

  class Solution {
  public:
      vector<int> twoSum(vector<int>& nums, int target)
      {
          std::unordered_map<int, int> track;
          std:vector<int> res;
          for(int index=0; index < nums.size(); index++)
          {
              int needed = target - nums[index];
              if(track.find(needed) != track.end())
              {
                  res.push_back(index);
                  res.push_back(track[needed]);
                  break;
              }
              else
              {
                  track[nums[index]] = index;
              }
          }
          return res;
      }
  };
  ```

<br>
<br>

## Resources

<br>
<br>
