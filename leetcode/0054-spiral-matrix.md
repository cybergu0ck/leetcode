# 54. Spiral Matrix

Medium [level question on leetcode](https://leetcode.com/problems/spiral-matrix/description/).

<br>
<br>
<br>

## Clarifications

* Are the elements unique in value?
    * Asking because having more data (even if not required) is always better.

* What are the minimum values of m and n?
    * `1 <= m, n <= 10`


<br>
<br>
<br>

## Test cases

| Case | Input | Output |
| ---- | ----- | ------ |
|  Sqaure matrix    |  [[1,2,3],[4,5,6],[7,8,9]]     |  [1,2,3,6,9,8,7,4,5]      |
|  Not a square matrix    |   [[1,2,3,4],[5,6,7,8],[9,10,11,12]]    |   [1,2,3,4,8,12,11,10,9,5,6,7]     |

<br>
<br>
<br>

## Solution

<br>
<br>

### Linear solution

```py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = left = 0
        bottom = len(matrix)-1
        right = len(matrix[0])-1

        direction = "go_right"
        res = []
        i = j = 0
        while top<=bottom and left<=right:
            res.append(matrix[i][j])
            if direction == "go_right":
                if j == right:
                    direction = "go_down"
                    i += 1
                    top += 1
                else:
                    j += 1
            elif direction == "go_down":
                if i == bottom:
                    direction = "go_left"
                    j -= 1
                    right -=1
                else:
                    i += 1
            elif direction == "go_left":
                if j == left:
                    direction = "go_up"
                    i -= 1
                    bottom -= 1
                else:
                    j -= 1
            else:
                if i == top:
                    direction = "go_right"
                    j += 1
                    left += 1
                else:
                    i -= 1

        return res 
```

```cpp

```

<br>

#### Explanation

Iterate over the matrix in spiral fashion by shrinking the boundaries.

* This is not a good solution but a brute force one I stumbled upo.
* Use four pointers to keep track of boundaries.
* Use two pointers to keep track of current cell.
* Use one variable to keep track of current direction.
    * This is needed because I found it difficult to code up the algo using only above variables, updating the boundaries was breaking the logic. Hence this extra variable.


<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(m*n)$ solution in terms of time, where $m$ and $n$ are number of rows and columns of the matrix.
    * Each cell of the matrix is visited only once.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.
    * Not accounting for the output array.

<br>
<br>

### Optimal linear solution

```py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1

        res = []
        while left<=right and top<=bottom:
            for col in range(left, right+1):
                res.append(matrix[top][col])
            top += 1

            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right -= 1

            if top <= bottom: #if top > bottom, it means all the cells are already covered
                for col in range(right, left-1,-1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            if left <= right: #if left > right, it means all the cells are already covered
                for row in range(bottom, top-1, -1):
                    res.append(matrix[row][left])
                left += 1
            
        return res
```

```cpp

```

<br>

#### Explanation

Iterate over the matrix in spiral fashion by shrinking the boundaries and utilize for loops.

* Use four variables to keep track of boudaries.
* Use four `for` loops to traverse the cells within the boundaries, one for each of right, down, left and up.
* Note that there is special case which needs a guard. This will go unnoticed while dry running if iterations are stopped without fully completing, at the end the above algorithm will continue even after tracing all the cells. This needs to avoided using the `if` conditionals. 

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(m*n)$ solution in terms of time, where $m$ and $n$ are number of rows and columns of the matrix.
    * Each cell of the matrix is visited only once.
- Space Complexity : This is a constant, $O(1)$ solution in terms of space.
    * Not accounting for the output array.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes


* This question is similar to drawing patterns like traingles, inverted triangles using `for` loops.
* When the use case is traversing directions. If the algorithm can't be coded using just the indicies, introducing an extra variable ([example](#linear-solution)) to track the direction will help. Although, there ideally exists an altogether better algorithm ([example](#optimal-linear-solution)).

<br>
<br>
<br>

## Resources


* The [optimal solution](#optimal-linear-solution) is from [Nikhil Lohia](https://www.youtube.com/watch?v=aqVW8IuXUF0).

<br>
<br>
<br>
