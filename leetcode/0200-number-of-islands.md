# 200. Number of Islands

Medium [level question on leetcode](https://leetcode.com/problems/number-of-islands/description/).

<br>
<br>
<br>

## Clarifications

No doubts.

<br>
<br>
<br>

## Test cases

| Case                       | Input                   | Output |
| -------------------------- | ----------------------- | ------ |
| Single cell with island    | [["1"]]                 | 1      |
| Single cell with no island | [["0"]]                 | 0      |
| 2\*2 with one island       | [["1", "1"],["0", "1"]] | 1      |
| 2\*2 with two island       | [["1", "0"],["0", "1"]] | 2      |

- Not really driven by test cases I think.

<br>
<br>
<br>

## Solution

<br>
<br>

### Linear solution

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visitedCells = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j]=="0" or (i,j) in visitedCells:
                return

            visitedCells.add((i,j))
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)

        numIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in visitedCells:
                    numIslands += 1
                    dfs(row,col)

        return numIslands

```

```cpp

```

<br>

#### Explanation

Use depth first search to visit every cell in the grid and check for islands.

- Code up the recursive solution.
  - multiple conditioned base case as follows:
    - The indices are invalid i.e. in the out of bounds of the grid.
    - The corresponding cell is a "0"
    - The corresponding cell is visited.
  - visit top, bottom, left and right cells recursively and mark each cell visited.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(m*n)$ solution in terms of time, where $m$ and $n$ are the rows and columns of the grid.
  - Each cell in the grid is visited only once.
  - Might look like quadratic but essentially it is linear especially considering the number of cells instead of row and column of grid.
- Space Complexity : This is a linear, $O(m*n)$ solution in terms of space, where $m$ and $n$ are the rows and columns of the grid.
  - Every cell in the grid is stored in the set.
  - There is also a recursion stack space which could go as deep as the total number of cells.

<br>
<br>

### Linear solution without using a data structure

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visitedCells = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j]=="0":
                return

            grid[i][j] = "0"
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)

        numIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    numIslands += 1
                    dfs(row,col)

        return numIslands
```

```cpp

```

<br>

#### Explanation

Exactly same algorithm as [linear solution](#linear-solution) but without a set datastructure.

- Cleaverly make the cell value "0" after visiting it.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(m*n)$ solution in terms of time, where $m$ and $n$ are the rows and columns of the grid.
  - Each cell in the grid is visited only once.
  - Might look like quadratic but essentially it is linear especially considering the number of cells instead of row and column of grid.
- Space Complexity : This is a linear, $O(m*n)$ solution in terms of space.
  - The space complexity is because of the recursion stack space which could go as deep as the total number of cells.

<br>
<br>

### Optimal linear iterative solution

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        numIslands = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    numIslands += 1
                    stack = [(row, col)]
                    while stack:
                        r,c = stack.pop()   #unpack

                        if r>=0 and c+1<n and grid[r][c+1] == "1":
                            #check right
                            grid[r][c+1] = "0"
                            stack.append((r,c+1))

                        if r>=0 and c-1>=0 and  grid[r][c-1] == "1":
                            #check left
                            grid[r][c-1] = "0"
                            stack.append((r,c-1))

                        if r+1<m and c>=0 and  grid[r+1][c] == "1":
                            #check bottom
                            grid[r+1][c] = "0"
                            stack.append((r+1,c))

                        if r-1>=0 and c>=0 and  grid[r-1][c] == "1":
                            #check top
                            grid[r-1][c] = "0"
                            stack.append((r-1,c))

        return numIslands
```

```cpp

```

<br>

#### Explanation

Implement iterative dfs and make visited cell values as "0".

- Utilise a stack.
- This has the same time and space complexities as before but it is better as recursion is avoided.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(m*n)$ solution in terms of time, where $m$ and $n$ are the rows and columns of the grid.
  - Each cell in the grid is visited only once.
  - Might look like quadratic but essentially it is linear especially considering the number of cells instead of row and column of grid.
- Space Complexity : This is a linear, $O(m*n)$ solution in terms of space.
  - The space complexity is because of size of the stack.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Know about Depth First Search.
  - DFS uses stack.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
