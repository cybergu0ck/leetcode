# Template

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://leetcode.com/problems/find-champion-ii/description/).

- Some good follow ups are:

  - Can there be an empty DAG? meaning individual teams exist where none are stronger nor weaker than other? Yes, there can be

  <br>
  <br>

## Test Cases

| Input                              | Output | Note                                                        |
| ---------------------------------- | ------ | ----------------------------------------------------------- |
| n=1, edges=[]                      | 0      | A single team (with index 0) exists thus it is the champion |
| n=2, edges=[]                      | 0      | Two teams are champtions                                    |
| n=3, edges=[[0,1]]                 | -1     | Two teams are champions                                     |
| n = 4, edges = [[0,2],[1,3],[1,2]] | -1     | Two teams are champions                                     |
| n = 3, edges = [[0,1],[1,2]]       | 0      | Team with index 0 is exists as a unique champ               |

<br>
<br>

## Solution

<br>

### Brute Force

```py
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        not_champs = []
        for pair in edges:
            not_champs.append(pair[1])
        champs = []
        for team in range(n):
            if team not in not_champs:
                champs.append(team)
        if len(champs) != 1:
            return -1
        else:
            return champs[0]
```

```cpp
#include <algorithm>
#include <vector>
class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        vector<int> not_champs;
        for(auto pair:edges){
            not_champs.push_back(pair[1]);
        }
        vector<int> champs;
        for(int i=0; i<n; ++i){
            if(std::find(not_champs.begin(), not_champs.end(), i) == not_champs.end()){
                champs.push_back(i);
            }
        }
        if(champs.size() != 1){
            return -1;
        }
        else{
            return champs[0];
        }
    }
};
```

- This is a linear $O(n)$ solution in terms of time, where $n$ is the greater among number of teams or number of edges .
- This is a linear $O(n)$ solution in terms of space, where $n$ is the number of non-champion teams .

<br>

### Efficient Solution

```py

```

```cpp

```

- This is a $O()$ solution in terms of time, where $ $ is .
- This is a $O()$ solution in terms of space, where $ $ is .

<br>
<br>

## Notes

- Use the algorithm library's find method to check if an element is present in the vector.

<br>
<br>

## Resources

<br>
<br>
