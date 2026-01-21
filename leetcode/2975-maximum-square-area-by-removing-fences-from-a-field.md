# 2975. Maximum Square Area by Removing Fences From a Field

Medium [level question on leetcode](https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/description/).

<br>
<br>
<br>

## Clarifications

- Took time and an example to understand the meaning of `hFences` and `vFences`.

- Can there be a case of no fences?
  - No, `1 <= hFences.length, vFences.length <= 600`
- Are all the values in fences valid?
  - Yes, `1 < hFences[i] < m` and `1 < vFences[i] < n`
- Are `hFences` and `vFences` sorted?
  - No
- Are `hFences` and `vFences` unique?
  - Yes

<br>
<br>
<br>

## Test cases

| Case                             | Input                                        | Output |
| -------------------------------- | -------------------------------------------- | ------ |
| Maximum square area possible     |                                              |        |
| Maximum square area not possible | m = 6, n = 7, hFences = [2], vFences = [4]   | -1     |
| Maximum square areas possible    | m = 4, n = 3, hFences = [2,3], vFences = [2] | 4      |

<br>
<br>
<br>

## Solution

<br>
<br>

### Quadrtic solution

```py
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def getAllSideDimensions(fences):
            sides = set()
            for i in range(len(fences)):
                for j in range(len(fences)):
                    if i != j:
                        sides.add(abs(fences[i]-fences[j]))
            return sides

        hFences = hFences + [1,m]
        vFences = vFences + [1,n]
        commonSides = getAllSideDimensions(hFences) & getAllSideDimensions(vFences)
        return ((max(commonSides)**2) % (10**9 + 7)) if commonSides else -1
```

```cpp

```

<br>

#### Explanation

Find all possible distances between horizontal fences (including boundaries) and repeat for vertical fences. The largest shared distance is the side of the maximum square.

- Include outer boundaries of the matrix in the fences list.
- Gather all possible unique side dimensions seperately (horizontal and vertical).
- The common elements in these represent possible square side dimensions.
  - Note that elements can be in any order. Squares can be formed inside the matrix as long as the sides are same.
- Return -1 if there are no common side, Otherwise return the square (after moding it as mentioned in the question) of the maximum common side.

<br>

#### Complexity analysis

- Time Complexity : This is a quadratic, $O(m^2+n^2)$ solution in terms of time, where $m$ and $n$ are the dimensions of the input matrix.
  - The nested loop calculates the distance between every fence position seperately for horizontal and vertical fences.

- Space Complexity : This is a quadratic, $O(m^2+n^2)$ solution in terms of space, where $m$ and $n$ are the dimensions of the input matrix.
  - The size of the set grows with the number of distances calculated.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Easy to implement the logic with the information that square by definiton have same side dimension.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
