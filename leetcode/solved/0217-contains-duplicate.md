# 217. Contains Duplicate

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/contains-duplicate/description/).

<br>
<br>

## Test Cases

| Input   | Output | Note                  |
| ------- | ------ | --------------------- |
| [1,2,1] | true   | Duplicate present     |
| [1,2,3] | false  | Duplicate not present |

<br>
<br>

## Solution

<br>

### Brute Force

```py
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
      for index1 in range(len(nums)):
          for index2 in range(len(nums)):
              if index1 != index2 and nums[index1] == nums[index2]:
                  return True
      return False
```

- This is a quadratic $O(n^2)$ solution in terms of time.
- This is a constant $O(1)$ solution in terms of space.

<br>

### Linear Solution

```py
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
      unique_nums = set()
      for num in nums:
          if num in unique_nums:
              return True
          else:
              unique_nums.add(num)
      return False
```

```cpp
#include <unordered_set>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen;
        for(const int& num : nums){
            if(seen.count(num) > 0)
                return true;
            seen.insert(num);
        }
        return false;
    }
};
```

- Utilise an unordered set and loop through the numbers.
- This is a linear $O(n)$ solution in terms of time.
- This is a linear $O(n)$ solution in terms of space.

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py

  ```

<br>
<br>

## Notes

- We can sort the array and then check the difference between two consecutive items, if it's zero then it means it is a duplicate. This will have $O(n*log(n))$

- Use the set's `count` method instead of `std::find`, The following code will throw a time limit exceed error in leetcode.

  ```cpp
  #include <unordered_set>

  class Solution {
  public:
      bool containsDuplicate(vector<int>& nums) {
          std::unordered_set<int> uniques;
          for(const int& num : nums){
              auto find = std::find(uniques.begin(), uniques.end(), num);
              if(find != uniques.end()){
                  return true;
              }
              else{
                  uniques.insert(num);
              }
          }
          return false;
      }
  };
  ```

<br>
<br>

## Resources

<br>
<br>
