# 1091. Shortest Path in Binary Matrix

Medium [level question on leetcode](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/).

<br>
<br>
<br>

## Objective

Return the length of the shortest clear path if present otherwise return -1.

<br>
<br>
<br>

## Clarifications

1. What is the minimum and maximum dimensions of the givem `n*n` matrix?
   - `1 <= n <= 100`

1. Any input constraints on the element, data type and values?
   - `grid[i][j] is 0 or 1`

1. Do we have the liberty to modify the type and value of the elements?
   - No constraint mentioned, so yes.

<br>
<br>
<br>

## Test cases

| Case                | Type  | Input                     | Output           |
| ------------------- | ----- | ------------------------- | ---------------- |
| Single cell         | size  | [[x]]                     | 1 if x==0 else 0 |
| Start blocked       | size  | [[1,0,0],[1,1,0],[1,1,0]] | -1               |
| End blocked         | size  | [[0,0,0],[1,1,0],[1,1,1]] | -1               |
| Path exists         | value | [[0,0,0],[1,1,0],[1,1,0]] | 4                |
| Path doesn't exists | value | [[0,0,0],[1,1,1],[1,1,0]] | -1               |
| Choose optimal      | value | [[0,0,0],[0,0,0],[0,0,0]] | 3                |

<br>
<br>
<br>

## Solution

<br>
<br>

### Linear solution

```py
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        if(grid[0][0] != 0 or grid[num_rows - 1][num_cols - 1] != 0):
            return -1

        if num_rows == 1 and num_cols == 1:
            return 1

        dirs = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,1], [1,-1], [-1,-1]]
        q = deque()
        q.append((0,0,1))
        grid[0][0] = 1
        while q:
            i,j,moves = q.popleft()
            if i == num_rows - 1 and j == num_cols - 1:
                    return moves
            for dr, dc in dirs:
                r = i + dr
                c = j + dc
                if r >= 0 and r < num_rows and c >= 0 and c < num_cols and grid[r][c] == 0:
                    q.append((r,c,moves+1))
                    grid[r][c] = 1
        return -1
```

```cpp

```

<br>

#### Explanation

Use BFS, track path length and mark cells as visited upon enqueuing to avoid duplicate processing.

- Check if start `grid[0][0]` or end `grid[N-1][N-1]` is blocked to immediately return -1.
- Initialize a BFS queue with `(0, 0, 1) `and mark `grid[0][0] = 1` as visited.
- Explore all 8 directional neighbors, pushing valid unvisited 0 cells with moves + 1 and marking them visited immediately.
- Return moves as soon as the bottom-right destination cell (N-1, N-1) is dequeued.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(N \times M)$ solution in terms of time, where $N$ and $M$ are the number of rows and columns in the grid.
  - Each cell in the grid is visited and processed at most once during the BFS traversal.

- Space Complexity : This is an $O(N \times M)$ solution in terms of space.
  - In the worst-case scenario, the BFS queue can store up to $O(N \times M)$ cell coordinates at a time.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Must know how to implement BFS.
- Know python collection module's "deque" and it's `append` and `popleft` methods.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
