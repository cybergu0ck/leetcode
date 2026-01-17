# 48. Rotate Image

Medium level question on [leetcode](https://leetcode.com/problems/rotate-image/description/).

<br>
<br>
<br>

## Clarifications

No doubts.

<br>
<br>
<br>

## Test cases

| Case         | Input                                            | Output                                           |
| ------------ | ------------------------------------------------ | ------------------------------------------------ |
| 1 x 1 matrix | [1]                                              | [1]                                              |
| 2 x 2 matrix | [[1,2],[3,4]]                                    | [[3,1],[4,2]]                                    |
| 3 x 3 matrix | [[1,2,3],[4,5,6],[7,8,9]]                        | [[7,4,1],[8,5,2],[9,6,3]]                        |
| 4 x 4 matrix | [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] | [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]] |

- Generally for a question of this kind, Pick a decent sized of matrix. Not too small (like 1x1, 2x2, 3x3) as they don't expose hidden details. Not too large (6x6 or above) as they are too time and effort consuming. If the algorithm works for something like a 4x4 or 5x5 matrix, it will most likely work for higher dimensions.

<br>
<br>
<br>

## Solution

<br>
<br>

### Quadratic solution with quadratic space

```py
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        copy = matrix.copy()

        for r in range(len(copy)):
            reverseColumn = [ copy[row][r] for row in range(len(copy)-1,-1,-1)]
            matrix[r] = reverseColumn
```

```cpp

```

<br>

#### Explanation

- Rotating a matrix is equvivalent to transposing the matrix and then reversing the values in each row.

  - Another way of saying the above is "reversing the transpose of columns".
  - This is done by:

    1. Iterating over the rows.
    1. Replacing each row with the reverse of the column values from the "original matrix".

       ```py
       reverseColumn = []
       for row in range(len(originalMatrix)-1,-1,-1):
           reverseColumn.append(originalMatrix[row][r]) #Here r is the row number from the outer iteration
       ```

  - Since each row is modified in the iteration process, we need to store a copy of the original matrix!
  - This is not the solution to the given question as it strictly instructs to not use additional space to store the matrix.

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(n^2)$ solution in terms of time, where $n$ is the dimension of the square matrix.
  - Each cell is visited only once.
- Space Complexity : This is a linear, $O(N)$ solution in terms of space, where $N$ is the total number of cells ($N=n^2$).
  - This is the space required to store the copy of the original matrix.

* The time and space complexity is quadratic in terms of the dimensions of the matrix but linear in terms of the number of cells i.e. $O(N)$, where $N$ is the number of cells.

<br>
<br>

### Quadratic solution with constant space

```py
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for layer in range(n//2):
            for offset in range(n-(2*layer)-1):
                #save the bottom left
                temp = matrix[n-1-layer-offset][layer]

                #update bottom left with bottom right
                matrix[n-1-layer-offset][layer] = matrix[n-1-layer][n-1-layer-offset]

                #update bottom right with top right
                matrix[n-1-layer][n-1-layer-offset] = matrix[layer+offset][n-1-layer]

                #update top right with top left
                matrix[layer+offset][n-1-layer] = matrix[layer][layer+offset]

                #update top left with temp
                matrix[layer][layer+offset] = temp
```

```cpp

```

<br>

#### Explanation

Performs a circular four-way swap of elements in concentric layers of the matrix.

- Layer by layer processing : Iteration is done starting from the outer loop and then towards the inner loop of the 2d matrix. (Think of an onion).
  - A 1x1, 2x2 and 3x3 (ignoring the inner cell) matrix have only 1 layer.
  - A 4x4 and 5x5 matrix (ignoring the inner cell) have 2 layers.
  - A 6x6 and 7x7 matrix (ignoring the inner cell) have 3 layers.
  - `range(n//2)` is essentially the number of layers for a given $n$.
- Four way swap : Pick one element from top, right, bottom and left corners and rotate them simultaneously. In the above algorithm,
  - The bottom left value is saved in a temporary.
  - The bottom left value is updated with bottom right value.
  - The bottom right value is updated with top right value.
  - The top right value is updated with top left value.
  - The top left value is updated with the tempoary.
- The `offset` variable is used to map the indicies for the four way swap accuately specific to the given layer.
  - For layer = 0 (outermost layer), $n-1$ swaps need to be done.
  - For layer = 1 , $n-3$ swaps need to be done.
  - For layer = 2 , $n-5$ swaps are required and so on.
  - `n-(2*layer)-1` uses the expression for odd number and achieves the equation for the above.

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(n^2)$ solution in terms of time, where $n$ is the dimension of the square matrix.
  - Each cell is visited only once.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.

* The time and space complexity is quadratic in terms of the dimensions of the matrix but linear in terms of the number of cells i.e. $O(N)$, where $N$ is the number of cells.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- This kind of questions are not really test case driven. Although pick a decent sized matrix (4x4 or 5x5) and dry run the algorithm, it will most likly scale for higher dimensions.
- Know about transpose of an array and matrix.
- Rotating a matrix is equvivalent to transposing the matrix and then reversing the values in each row.

Python :

- `//` is floor division operator, gives the floor of the quotient.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
