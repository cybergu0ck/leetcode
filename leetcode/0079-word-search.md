# 79. Word Search

Medium [level question on leetcode](https://leetcode.com/problems/word-search/).

<br>
<br>
<br>

## Clarifications

1. What is the minimum and maximum dimensions of the givem `m*n` matrix?
   - `1 <= m, n <= 6`

1. Any input constraints on the element, data type and values?
   - Board consists of lower case and upper case english letters.

1. Do we have the liberty to modify the type and value of the elements?
   - Yes

1. Can the matrix be empty?
   - No

<br>
<br>
<br>

## Test cases

| Case        | Input                                                                            | Output |
| ----------- | -------------------------------------------------------------------------------- | ------ |
| Found       | board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED" | true   |
| Not found   | board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABZCED" | false  |
| Revist case | board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"   | false  |

<br>
<br>
<br>

## Solution

<br>
<br>

### Exponential solution

```py
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c, index):
            if index == len(word):
                return True

            if r<0 or c<0 or r>=rows or c>=cols or word[index] != board[r][c]:
                return False

            #save the current character and tag it as visited for current step of recursion
            temp = board[r][c]
            board[r][c] = '#'

            #dfs
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in dirs:
                if dfs(r+dr, c+dc, index + 1):
                    return True

            #assign the original character back
            board[r][c] = temp

            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c, 0):
                        return True

        return False
```

```cpp

```

<br>

#### Explanation

Initiate a DFS from every cell matching the word's first character, recursively exploring four-directional paths by comparing the current cell to the character at the target index.

- Trigger: Iterate through the grid and initiate DFS only when a cell matches the first character of the word.
- Parameters: Pass the current coordinates $(r, c)$ and the target index of the character being matched.
- Success Base Case: If the index equals the word length, return True (word fully found).
- Failure Base Case: Return False if coordinates are out of bounds or board[r][c] does not match word[index].
- Recursively call DFS for all four neighbors.
- It is important to not revist the cells that are already visited, it is done by "tagging" or "marking" in-place temporarily for the specific step of recursion.
  - Temporarily mark the cell as visited (e.g., board[r][c] = '#') to prevent reuse.
  - Restore the cell's original value after the recursive calls (backtrack).
- Early Exit: Use short-circuiting to return True immediately if any neighbor returns a success.

<br>

#### Complexity analysis

- Time Complexity : This is a exponential, $O(m*n*4^k)$ solution in terms of time, where $m$,$n$ and $k$ are number of rows, columns and the length of the input word.
  - The outer nested loop is of $O(m*n)$.
  - The time complexity is determined by the number of recursive calls which is equal to the number of nodes in the recursive tree. The maximum number of nodes in a tree with depth of $n$ and each node having $k$ branches is
    $$\frac{k^{(n+1)} - 1}{k - 1}$$
  - The dfs function is $O(4^k)$. We can see that the number of branches is 4 (The four directions) and the depth is the length of the input word.

- Space Complexity : This is a linear, $O(k)$ solution in terms of space, where $k$ is the length of the input word.
  - This is the space of the recursion stack.

<br>
<br>

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- It is important to add a test case where revisting the cells is considered.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
