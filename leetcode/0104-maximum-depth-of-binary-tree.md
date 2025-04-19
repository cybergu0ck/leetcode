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

## Notes

- The question mentions that "A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.", but textbook definition of depth uses the number of edges instead of the nodes (I'm guessing). To get the maximum depth of the binary tree in terms of edges,

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
