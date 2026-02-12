# 417. Pacific Atlantic Water Flow

Medium [level question on leetcode](https://leetcode.com/problems/pacific-atlantic-water-flow/description/).

<br>
<br>
<br>

## Clarifications

<br>
<br>
<br>

## Test cases

| Case                           | Input                                                         | Output                                      |
| ------------------------------ | ------------------------------------------------------------- | ------------------------------------------- |
| matrix with 1 row and 1 column | [[1]]                                                         | [[0,0]]                                     |
| matrix with only row           | [[1,2,3]]                                                     | [[0,0],[0,1],[0,2]]                         |
| matrix with only column        | [[1],[2],[3]]                                                 | [[0,0],[1,0],[1,1]]                         |
| square matrix                  | [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]] | [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]] |
| non-square matrix              | [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1]]                         | [[0,4],[2,1],[2,0],[1,4],[2,2],[1,0],[1,3]] |

- Although the algorithm should be driven not by test cases for this kind of question.
- Having test cases is anyway useful to test the algorithm.

<br>
<br>
<br>

## Solution

<br>
<br>

### Linear recursive solution

```py
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c, visited):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited:
                return

            visited.add((r,c))

            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                if r+dr>=0 and c+dc>=0 and r+dr < rows and c+dc < cols and heights[r+dr][c+dc] >= heights[r][c]:
                    dfs(r+dr, c+dc, visited)

        pacific = set()
        atlantic = set()
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols-1, atlantic)

        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows-1, c, atlantic)

        return [list(item) for item in pacific if item in atlantic]
```

```cpp

```

<br>

#### Explanation

Starting from the ocean, seek all the cells that can contain water flow using DFS.

- Instead of going cell by cell towards the opposite oceans, a much simpler way to solve this is to flip the approach.
- From the ocean boundaries, see which cells can contain water flow.
  - Use top most and left most cells and mark all the cells that can contain water flow that leads to pacific ocean.
  - Use bottom most and right most cells and mark all the cells that can contain water flow that leads to atlantic ocean.
- Since we are going the opposite way the condition will have to be tweaked, the current cell must be less than over equal to the next cell.
- Use classic recursive DFS template.
- Apply DFS on each node such that each node once for pacific search and once for atlantic search.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(m*n)$ solution in terms of time, where $m$ and $n$ are the number of rows and columns of the given matrix.
  - In the worst case, every cell is visited twice. Once for pacific search and one for atlantic search.
- Space Complexity : This is a lienar, $O(m*n)$ solution in terms of space, where $m$ and $n$ are the number of rows and columns of the given matrix.
  - In the worst case for a flat grid (no elevation), both the set's would store $m*n$ values.
  - The recursion stack.
  - The output array.
- Although the notation is written in terms of rows and columns, essentially the complexity is considered linear in terms of the number of cells. $n=m*n$.

<br>
<br>
<br>

### Linear iterative solution

```py
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c, visited):
            stack = [(r,c)]
            while stack:
                r,c = stack.pop()
                if(r,c) not in visited:
                    visited.add((r,c))
                    directions = [[1,0], [-1,0], [0,1], [0,-1]]
                    for dr, dc in directions:
                        if r+dr>=0 and c+dc>=0 and r+dr < rows and c+dc < cols and heights[r+dr][c+dc] >= heights[r][c]:
                            stack.append((r+dr, c+dc))

        pacific = set()
        atlantic = set()
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols-1, atlantic)

        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows-1, c, atlantic)

        return [list(item) for item in pacific if item in atlantic]
```

<br>

#### Explanation

Starting from the ocean, seek all the cells that can contain water flow using DFS iteratively.

- The core logic is the same as [recursive solution](#linear-recursive-solution) but backtracking is done using a stack instead of recursion.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(m*n)$ solution in terms of time, where $m$ and $n$ are the number of rows and columns of the given matrix.
  - In the worst case, every cell is visited twice. Once for pacific search and one for atlantic search.
- Space Complexity : This is a lienar, $O(m*n)$ solution in terms of space, where $m$ and $n$ are the number of rows and columns of the given matrix.
  - In the worst case for a flat grid (no elevation), both the set's would store $m*n$ values.
  - The output array.
- Although the notation is written in terms of rows and columns, essentially the complexity is considered linear in terms of the number of cells. $n=m*n$.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- The following was my original implementation, all the if blocks inside the `dfs` function can be avoided by using a direction array as done in [optimal solution](#linear-iterative-solution).

  ```py
  class Solution:
      def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
          pacific = set()
          atlantic = set()
          maxRows = len(heights)
          maxCols = len(heights[0])

          def dfs(i,j, ds):
              cur = (i,j)
              if cur not in ds:
                  ds.add(cur)
                  row = cur[0]
                  col = cur[1]
                  if row+1 >=0 and row+1< maxRows and col>=0 and col< maxCols and heights[row+1][col] >= heights[row][col]:
                      dfs(row+1,col, ds)
                  if row-1 >=0 and row-1< maxRows and col>=0 and col< maxCols and heights[row-1][col] >= heights[row][col]:
                      dfs(row-1,col, ds)
                  if row >=0 and row< maxRows and col+1>=0 and col+1< maxCols and heights[row][col+1] >= heights[row][col]:
                      dfs(row,col+1, ds)
                  if row >=0 and row < maxRows and col-1>=0 and col-1< maxCols and heights[row][col-1] >= heights[row][col]:
                      dfs(row,col-1, ds)

          for i in range(maxRows):
              dfs(i,0, pacific)
              dfs(i, maxCols-1, atlantic)
          for i in range(maxCols):
              dfs(0,i, pacific)
              dfs(maxRows-1,i,atlantic)

          res = []
          for item in pacific:
              if item in atlantic:
                  res.append(list(item))
          return res
  ```

<br>
<br>
<br>

## Resources

- Followed [neetcode's](https://www.youtube.com/watch?v=s-VkcjHqkGI) video.

<br>
<br>
<br>
