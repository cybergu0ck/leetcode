# Same Tree

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://rebrand.ly/zzen77f).

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
      def isSameTree(self, p, q):
          if p and q:
              return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
          return p is q
  ```

  - The time complexity of the above algorithm depends on the number of recursive calls. The worst case will be when both the trees are identical, then the number of recursive calls will be equal to the number of nodes. Hence, $O(n)$.
  - The space complexity of the above algorithm depens on the depth of recursive. Hence, $O(n)$.

  - The last line `return p is q` is to return `True` if both p and q are not TreeNode and return `False` when one is TreeNode and other is not. Illustrated below.
  
    ```py
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def isSameTree(self, p, q):
            if p and q:
                return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                if not p and not q:
                    return True
                else:
                    return False
    ```

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
