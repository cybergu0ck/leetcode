# Invert Binary Tree

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://shorturl.at/Lq38f).

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

- The following has $O(n)$ time complexity $O(n)$ space complexity.

  ```py
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
          if not root:
              return
          else:
              root.left, root.right = root.right, root.left
          
          self.invertTree(root.left)
          self.invertTree(root.right)
          return root
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

<br>
<br>

## Resources

<br>
<br>
