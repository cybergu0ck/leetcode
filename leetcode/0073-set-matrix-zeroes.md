# 73. Set Matrix Zeroes

Medium [level question on leetcode](https://leetcode.com/problems/set-matrix-zeroes/description/).

<br>
<br>
<br>

## Clarifications

1. What is the minimum and maximum dimensions of the givem `m*n` matrix?
   - `1 <= m, n <= 200`

1. Any input constraints on the element, data type and values?
   - `2^31 <= matrix[i][j] <= 2^31 - 1`

1. Do we have the liberty to modify the type and value of the elements?
   - Algorithm can be designed if cell values can be modified to some other type.
   - Should ask this question upfront, I came up with this question after solving.

1. Can the matrix be empty?
   - No, see the minimum dimensions

<br>
<br>
<br>

## Test cases

| Case                                               | Input                           | Output                          |
| -------------------------------------------------- | ------------------------------- | ------------------------------- |
| Matrix with 1 row and 1 column containing non-zero | [[2]]                           | [[2]]                           |
| Matrix with 1 row and 1 column containing zero     | [[0]]                           | [[0]]                           |
| Square matrix                                      | [[1,1,1],[1,0,1],[1,1,1]]       | [[1,0,1],[0,0,0],[1,0,1]]       |
| Non square matrix                                  | [[0,1,2,0],[3,4,5,2],[1,3,1,5]] | [[0,0,0,0],[0,4,5,0],[0,3,1,0]] |

<br>
<br>
<br>

## Solution

<br>
<br>

### Linear solution if modification of type is allowed

```py
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def doesRowOrColumnContainZero(row, col):
            """
            helper function that returns True if either row or column contains zero
            """
            for item in matrix[row]:
                if item == 0:
                    return True
            for item in [row[col] for row in matrix]:
                if item == 0:
                    return True
            return False

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if doesRowOrColumnContainZero(row, col) and matrix[row][col] != 0:
                    matrix[row][col] = "True"   #Marking

        #Modify the marks to zero
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "True":
                    matrix[row][col] = 0
```

```cpp

```

<br>

#### Explanation

Iterate over the cells and mark the cell by changing the datatype if the corresponsing row or column has zero. Iterate once again and modify the marks to zeros.

- Code a helper function which takes in row and column indices and returns True if corresponding row or column contains zero.
- Iterate over the cells, check if the cell has to be made zero using the helper function. Mark it by changing the data type.
- Iterate over the cells, if the cell is marked make them zero.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(m*n)$ solution in terms of time, where $m$ and $n$ are dimensions of the given matrix.
  - Time complexity is linear in terms of cells, can be considered as quadratic in terms of the whole matrix (I guess).
  - Each cell is visited only once. (Technically twice but separate nested loops).
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.
  - Additional datastructures are not used.

<br>
<br>

### Linear solution

```py
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numRows = len(matrix)
        numCols = len(matrix[0])
        firstRowHasZero = firstColumnHasZero = False

        #check if zeros are present in first row and first column
        for row in matrix[0]:
            if row == 0:
                firstRowHasZero = True

        for col in [row[0] for row in matrix]:
            if col == 0:
                firstColumnHasZero = True

        #Iterate over the other rows and use first row and column for marking
        for row in range(1, numRows):
            for col in range(1, numCols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        #Iterate over the other rows and make zeros based on markers
        for row in range(1,numRows):
            for col in range(1,numCols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        #Make first row or column zero if it had any zeros
        if firstRowHasZero:
            for col in range(numCols):
                matrix[0][col] = 0
        if firstColumnHasZero:
            for row in range(numRows):
                matrix[row][0] = 0
```

```cpp

```

<br>

#### Explanation

Use the first row and first column for marking and then use it later to make zeros.

- This is a clever solution compared to [above solution](#linear-solution-if-modification-of-type-is-allowed).
- Cache if first row or column contains zero to begin with.
- Iterate over the remaining cells. If a cell is zero, mark the corresponsing indices in first row and first column.
- Iterate over the remaining cells again, use the markings in first row and first column and make zeros.
- Make first row and first column zero based on the original condition.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(m*n)$ solution in terms of time, where $m$ and $n$ are dimensions of the given matrix.
  - Time complexity is linear in terms of cells, can be considered as quadratic in terms of the whole matrix (I guess).
  - Each cell is visited only once. (Technically twice but separate nested loops).
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.
  - Additional datastructures are not used.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Difficult to come up with the [clever solution](#linear-solution) for the very first time. It is one of those approaches that needs to be unlocked for the brain! Got the algo from GPT.

<br>

Python:

- Getting $i'th$ column values from a matrix, specifically 2D list.

  ```py
  matrix = [[1,2,3],[4,5,6]]
  i = 0 #for first column
  columnValues = [row[i] for row in matrix]
  #[1,4]
  ```

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
