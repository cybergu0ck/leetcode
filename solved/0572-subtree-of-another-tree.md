# Subtree of Another Tree

Easy level question on leetcode.

<br>
<br>

## Description

Find it [here](https://shorturl.at/MWP2V).

<br>
<br>

## Solution

<br>

### Brute Force

- The following has $O(n^2)$ time complexity $O(n^2)$ space complexity.

  ```py
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def isSametree(self, p, q):
          if not p and not q:
              return True
          elif p and q and p.val == q.val:
              return self.isSametree(p.left,q.left) and self.isSametree(p.right, q.right)
          else:
              return False

      def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
          q = [root]
          while q:
              cur = q.pop(0)
              check = self.isSametree(cur,subRoot)
              if check:
                  return True
              if cur.left:
                  q.append(cur.left)
              if cur.right:
                  q.append(cur.right)
          
          return False
  ```

  - The time complexity is $O(n^2)$ because the bfs algorithm scales $O(n)$ and the algorithm to check same trees, being a recursive algorithm also takes $O(n)$.
  - The space complexity is $O(n)$ because the bfs algorithm uses a queue and the algorithm to check same trees, being a recursive algorithm also takes $O(n)$ space for the stack frames.

<br>

### Efficient Force

- The following has $O()$ time complexity $O()$ space complexity.

  ```py
  ```

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py
  ```

<br>
<br>

## Notes

- The most intuitive approach is the one in the brute force section, where we apply the BFS traversal with the algorithm to check if two trees are the same.

<br>
<br>

## Resources

<br>
<br>
