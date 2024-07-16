# Binary Tree Level Order Traversal

Medium level question on leetcode.

<br>
<br>

## Description

Find it [here](https://shorturl.at/89NnQ).

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
      def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
          res = []
          if root:
              q = [root]
              while q:
                  level = []
                  original_size = len(q)
                  while original_size>0:
                      cur = q.pop(0) #Remeber to pop the first value, It is a Queue!
                      level.append(cur.val)
                      original_size -=1
                      if cur.left:
                          q.append(cur.left)
                      if cur.right:
                          q.append(cur.right)
                  res.append(level)
          return res
  ```

 - Althought there are two while loops in the above code, it must not be confused for $O(n^2)$. The inner loop will process the specific nodes present for every level, it will never process the node twice. Hence the time complexity is bounded by the outer loop which will process each node in the tree, Hence, $O(n)$.
 - As we are using a queue, In the worst case the maximum size of queue would be $\frac{n}{2}$, which is still $O(n)$.

<br>

### Ideal Solution

- The following has $O()$ time complexity $O()$ space complexity.

  ```py
  ```

<br>
<br>

## Notes

- Note the usage of a counter (`original_size`), we can iterate over the list and keep updating (appending in this case) without the sideaffect of the update.

<br>
<br>

## Resources

<br>
<br>
