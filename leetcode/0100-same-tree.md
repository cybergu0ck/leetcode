# 100. Same Tree

Easy [level question on leetcode](https://leetcode.com/problems/same-tree/).

<br>
<br>
<br>

## Clarifications

Question is self explanatory.

<br>
<br>
<br>

## Test cases

| Case                                | Input                     | Output |
| ----------------------------------- | ------------------------- | ------ |
| same structure and values           | p = [1,2,3], q = [1,2,3]  | True   |
| same structure but different values | p = [1,2,1], q = [1,1,2]  | False  |
| different structure                 | p = [1,2], q = [1,null,2] | False  |

- The above test cases are complete for the given question.

<br>
<br>
<br>

## Solution

<br>
<br>

### Efficient solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(not p and not q):
            return True
        elif(p and q and p.val != q.val):
            return False
        elif((p and not q) or (q and not p)):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

```cpp

```

<br>

#### Explanation

Recursively check both nodes for existance and value for both left and right subtrees.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of nodes in the binary tree.

  - The time complexity depends on the number of recursive calls.
  - In the worst case when both trees are identical, the number of recusrive calls will be equal to the number of nodes.

- Space Complexity : This is a linear, $O(h)$ solution in terms of space, where $h$ is the depth of the binary tree.
  - In the worst case where the binary tree is skewed, the space complexity is $O(n)$ where $n$ is the number of nodes in the binary tree.
  - In the best case where the binary tree is balanced, the space complexity is $O(log(n))$ where $n$ is the number of nodes in the binary tree.

<br>
<br>
<br>

## Follow ups

<br>
<br>
<br>

## Notes

<br>
<br>
<br>

## Resources

<br>
<br>
<br>
