# 104. Maximum Depth of Binary Tree

Easy [level question on leetcode](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/).

<br>
<br>
<br>

## Clarifications

- Confirm the definition of depth of a binary tree. Is it based on number of edges or number of nodes?
  - It is mentioned that "A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node". Hence, we number of nodes is to be considered.

<br>
<br>
<br>

## Test cases

| Case | Input                          | Output |
| ---- | ------------------------------ | ------ |
|      | root = [3,9,20,null,null,15,7] | 3      |
|      | root = [1,null,2]              | 2      |

<br>
<br>
<br>

## Solution

<br>
<br>

### Recursive solution

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))
```

```cpp

```

<br>

#### Explanation

Recursively exlore left and right subtrees, add one to the depth of each level and return maximum found between the two subtrees.

<br>

#### Complexity analysis

- Time Complexity : This is a linear, $O(n)$ solution in terms of time, where $n$ is the number of nodes in the binary tree.

  - The time complexity is based on the number of times the recursive function is called. The recursive function is called once for every node in the binary tree.

- Space Complexity : This is a linear, $O(h)$ solution in terms of space, where $h$ is the depth of the binary tree.
  - In the worst case where the binary tree is skewed, the space complexity is $O(n)$ where $n$ is the number of nodes in the binary tree.
  - In the best case where the binary tree is balanced, the space complexity is $O(log(n))$ where $n$ is the number of nodes in the binary tree.

<br>
<br>
<br>

## Follow ups

- If depth is defined in terms of number of edges instead of number of nodes:

  ```py
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def maxDepth(self, root: Optional[TreeNode]) -> int:
          if(not root):
              return -1
          return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))
  ```

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
