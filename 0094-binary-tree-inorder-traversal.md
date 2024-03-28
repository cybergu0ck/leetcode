# Binary Tree Inorder Traversal

Leetcode easy level question.

<br>
<br>

## Description

Find it [here](http://rb.gy/76tm22)

<br>
<br>

## Solution

<br>

- $O(n)$ solution.

  ```py
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
          res = []
          stack = []
          cur = root
          while True:
              if cur:
                  stack.append(cur)
                  cur = cur.left
              elif stack:
                  cur = stack.pop()
                  res.append(cur.val)
                  cur = cur.right
              else:
                  break
          return res
  ```

<br>
<br>

## Resources

<br>
<br>
