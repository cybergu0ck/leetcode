# 217. Contains Duplicate

Easy [level question on leetcode](https://leetcode.com/problems/contains-duplicate/description/).

<br>
<br>
<br>

## Clarifications

<br>
<br>
<br>

## Test cases

| Case                  | Input     | Output |
| --------------------- | --------- | ------ |
| Contains duplicate    | [1,2,3,1] | true   |
| Contains no duplicate | [1,2,3,4] | false  |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
      for index1 in range(len(nums)):
          for index2 in range(len(nums)):
              if index1 != index2 and nums[index1] == nums[index2]:
                  return True
      return False
```

```cpp

```

<br>

#### Explanation

Perform nested iterations and check for duplicates for all possible comparisions.

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(n^2)$ solution in terms of time, where $n$ is size of the input array.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

<br>
<br>

### Linear solution

```py
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
      unique_nums = set()
      for num in nums:
        if num in unique_nums:  #O(1)
            return True
        else:
              unique_nums.add(num)
      return False
```

```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen;
        for(const auto& num : nums){
            auto[itr, res] = seen.insert(num); //O(1)
            if (!res){
                return true;
            }
        }
        return false;
    }
};
```

<br>

#### Explanation

Utilize a set.

- Iterate over every element in the input array, keep adding and checking in the set.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is size of the input array.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space. (Its $O(n)$ if the array itself is considered)

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

Python :

- Know the set's `add` method.

C++ :

- Understand about set's `insert` function, it's return value.
- Understand unpacking in C++. `auto[itr, res] = seen.insert(num);`
- Note that time complexity of set's `insert` is $O(1)$ on average.
- Checking for an element in the set using algorithm's `find` method takes $O(n * log(n))$.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
