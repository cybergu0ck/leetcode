# Maximum Depth of Binary Tree

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://rebrand.ly/d4i7n5s).

<br>
<br>

## Solution

<br>

### Brute Force

- The following has $O()$ time complexity $O()$ space complexity.

  ```py
  ```

<br>

### Efficient Force

- The following has $O(N)$ time complexity $O(N)$ space complexity.

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
              return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
  ```

  - The time complexity for a recusrsive algorithm depends on the number of recursive calls. In the worst case, the number of recursive calls in the above algorithm will be equal to the number of nodes. Hence, $O(n)$.
  - The space complexity for a recursive algorithm depends on the depth of the recursion (the stack). Hence, $O(n)$.

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py
  ```

<br>
<br>

## Notes

- The question mentions that  "A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.", but textbook definition of depth uses the number of edges instead of the nodes (I'm guessing). To get the maximum depth of the binary tree in  terms of edges, 

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
              return -1
          else:
              return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
  ```

<br>
<br>

## Resources

<br>
<br>
