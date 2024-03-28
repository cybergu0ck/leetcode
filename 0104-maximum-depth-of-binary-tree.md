# Maximum Depth of Binary Tree

Easy level problem on leetcode.

<br>
<br>

## Description

Find it [here](http://rb.gy/elm162)

<br>
<br>

## Solution

### Brute Force

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
```

<br>
<br>

## Resources
