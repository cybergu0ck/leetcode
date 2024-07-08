# Reverse Linked List

Leetcode medium level question.

<br>
<br>

## Description

Find it [here](https://rebrand.ly/bb0tuzm)

<br>
<br>

## Solution

<br>

- $O(n)$ solution. Use in-order binary tree traversal logic, which is a DFS algorithm. Use a counter to keep track of the number of nodes traversed and make a early return. 

  ```py
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        stack = []
        n = 0  
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                n += 1
                if(n == k):
                    return cur.val
                else:
                    cur = cur.right
            else:
                break  
  ```

<br>
<br>

## Resources

<br>
<br>
