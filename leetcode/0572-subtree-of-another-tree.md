# 572. Subtree of Another Tree

Easy [level question on leetcode](https://leetcode.com/problems/subtree-of-another-tree/description/).

<br>
<br>
<br>

## Clarifications

- Among p and q, is q always the root node for the subRoot (The tree which is present as a subtree in the other)?

  - Yes

- Can p and q be the same? Implying that a tree can be considered a subtree of itself?

  - Yes

<br>
<br>
<br>

## Test cases

| Case                    | Input                                                       | Output |
| ----------------------- | ----------------------------------------------------------- | ------ |
| q is a subtree of p     | root = [3,4,5,1,2], subRoot = [4,1,2]                       | true   |
| q is not a subtree of p | root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] | false  |
| both p and q are same   | root = [3,4,5,1,2], subRoot = [3,4,5,1,2]                   | true   |

- The above test cases are complete for the given question.

<br>
<br>
<br>

## Solution

<br>
<br>

### Brute force

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p,q) -> bool:
            if(not p and not q):
                return True
            elif(p and q and p.val != q.val):
                return False
            elif((p and not q) or (q and not p)):
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def rec(p,q):
            if not p:
                return False
            elif isSameTree(p, q):
                return True
            return rec(p.left, q) or rec(p.right, q)

        return rec(root, subRoot)


```

```cpp

```

<br>

#### Explanation

Traverse the tree and check if subTree is same as the tree rooted at current node.

<br>

#### Complexity analysis

- Time Complexity : This is a bilinear, $O(n*m)$ solution in terms of time, where $n$ is the number of nodes in the tree rooted at `root` and $m$ is the number of nodes in the tree rooted at `subRoot`.

  - The time complexity of `isSameTree` is $O(m)$, where $m$ is the number of nodes in tree rooted at `subRoot`.
  - The time complexity of `rec` is $O(n)$, where $n$ is the number of nodes in the tree rooted at `root`.
  - Overall, the time complexiy would be $O(n*m)$.

- Space Complexity : This is a bilinear, $O(n*m)$ solution in terms of space because of recursive call stacks.
  - Using an iterative traversal algorithm would be good and it would reduce the space complexity to linear.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

- Use an iterative traversal algorithm, like a DFS instead of the recursive one used above.

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
