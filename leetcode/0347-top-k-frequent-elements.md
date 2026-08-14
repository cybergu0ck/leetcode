# 347. Top K Frequent Elements

Medium [level question on leetcode](https://leetcode.com/problems/top-k-frequent-elements/description/).

<br>
<br>
<br>

## Clarifications

1. Is the array sorted?
   - No

1. Is the array comprised of unique elements?
   - No

1. What is the type of data stored in the array?
   - Integers

1. Can the array be modified?
   - A new array to be returned.

1. Can the array be empty?
   - Yes

1. Is "k" always valid?
   - Yes, a test case like [1,2,3] and k=1 is not valid.

<br>
<br>
<br>

## Test cases

| Case       | Input                    | Output |
| ---------- | ------------------------ | ------ |
| Basic case | [1,3,3,5,5,5,10] and k=2 | [5,3]  |

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute logarithmic solution

```py
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #form the map; O(n)
        numToFrequency = defaultdict(int)
        for num in nums:
            numToFrequency[num] += 1

        #sort the dict based on the value, get the list of the sorted keys, reverse the list; O(n*logn)
        sortedPairs = sorted(numToFrequency.items(), key = lambda pair:pair[1])
        sortedPairs.reverse()

        #populate and return the result; O(k)
        res = list()
        for i in range(k):
            res.append(sortedPairs[i][0])

        return res
```

```cpp
#include <unordered_map>
#include <vector>
#include <utility>
#include <algorithm>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> num_to_count;
        for(const auto& num : nums){    //O(n)
            ++num_to_count[num];
        }

        std::vector<std::pair<int,int>> temp_vec;
        for(const auto& pair : num_to_count){
            temp_vec.push_back(pair);
        }

        std::sort(temp_vec.begin(), temp_vec.end(), [](std::pair<int,int> a, auto b){return a.second > b.second;});   //mO(m)

        std::vector<int> res;
        for(int i=0; i < k; ++i){
            res.push_back(temp_vec[i].first);
        }

        return res;
    }
};
```

<br>

#### Explanation

Use a map.

- Use a map with keys as the unique elements and values as the frequency.
- Sort the map based on the values.
- Get the top "k" frequent values.

<br>

#### Complexity analysis

- Time Complexity : This is a logarithmic, $O(n*log(n))$ solution in terms of time, where $n$ is number of elements in the given array.
  - $O(n)$ to form the map.
  - $O(n*log(n))$ to sort the map.
  - $O(k)$ to iterate over the map "k" times, here "k" is the given input.
  - Overall, the time complexity is $O(n) + O(n*logn) + O(k)$ and the logarithmic component dominates.
- Space Complexity : This is a lienar, $O(n)$ solution in terms of space, where $n$ is number of elements in the given array.
  - This is the space taken by the map.

<br>
<br>

### Linear solution

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #form the map
        from collections import defaultdict
        numToFrequency = defaultdict(int)
        for num in nums:
            numToFrequency[num] += 1

        #populate the buckets
        buckets = [[] for i in range(len(nums))]
        for key,value in numToFrequency.items():
            buckets[value-1].append(key)

        #return top k elements
        res = []
        for i in range(len(buckets)-1,-1,-1):
            if k <= 0:
                break
            if len(buckets[i]) != 0:
                res.extend(buckets[i])
                k -= len(buckets[i])

        return res
```

````

```cpp

````

<br>

#### Explanation

Use a variant of bucket sort.

- Use a map with keys as elements and values as frequency of the corresponding elements.
- Use an array for bucketing.
  - The indicies of this array is the frequency of the element. Example : Third index reperesents elements repeating three times.
  * The elements of this array will be an array containing the numbers.
  - Populate this array using the populated map.
- Iterate over the array and return the top "k" frequent elements.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is number of elements in the given array.
  - $O(n)$ to form the map.
  - $O(n)$ to form the frequency array.
  - $O(k)$ to iterate over the map "k" times, here "k" is the given input.
  - Overall, the time complexity is $O(n) + O(n) + O(k)$.
- Space Complexity : This is a lienar, $O(n)$ solution in terms of space, where $n$ is number of elements in the given array.
  - This is the space taken by the map and the array.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Know about bucket sorting. <!-- //TODO - Add notes on bucket sorting in the notes repo and link it here -->
- About sorting a map based on the values.

<br>

Python :

1. Python list's `reverse` method reverses the list in-place and returns `None`

   ```py
   arr = [i for i in range(10)].reverse()
   print(arr)

   # None
   ```

1. Python list's `extend` method facilitates combining elements of one array to another.

   ```py
   arr = [1,2,3]
   arr.extend([5,10])
   print(arr)

   # [1, 2, 3, 5, 10]
   ```

1. Know about "defaultdicts"

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
```
